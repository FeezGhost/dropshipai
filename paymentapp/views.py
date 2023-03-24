from django.shortcuts import redirect
from rest_framework.views import APIView
import stripe
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from django.utils import timezone

from django.contrib.auth.models import User

stripe.api_key = settings.STRIPE_SEC_KEY
webhook_secret = settings.STRIPE_WEBHOOK_SECRET

FRONTEND_CHECKOUT_SUCCESS_URL = settings.CHECKOUT_SUCCESS_URL
FRONTEND_CHECKOUT_FAILED_URL = settings.CHECKOUT_FAILED_URL

# Create your views here.
class CreateCheckoutSession(APIView):
  def get(self, request, pk_id):
    user_id = pk_id
    price = settings.STRIPE_PRICE_KEY
    print('user_id', user_id)
    try:
      checkout_session = stripe.checkout.Session.create(
        client_reference_id=user_id,
        line_items = [{
            'price': price,
            'quantity': 1,
        }],
        mode= 'subscription',
        success_url= FRONTEND_CHECKOUT_SUCCESS_URL,
        cancel_url= FRONTEND_CHECKOUT_FAILED_URL,
      )
      print("checkout session created", checkout_session)
      return redirect(checkout_session.url , code=303)
    except Exception as e:
        print(e)
        return e
    
class WebHook(APIView):
  def post(self , request):
    event = None
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
      event = stripe.Webhook.construct_event(
        payload ,sig_header , webhook_secret
        )
    except ValueError as err:
        # Invalid payload
        print('value error',err)
        raise err
    except stripe.error.SignatureVerificationError as err:
        # Invalid signature
        print('signature error', err)
        raise err

    # Handle the event
    if event.type == 'payment_intent.succeeded':
      payment_intent = event.data.object 
      print("--------payment_intent ---------->" , payment_intent)
    elif event.type == 'payment_method.attached':
      payment_method = event.data.object 
      print("--------payment_method ---------->" , payment_method)
    # ... handle other event types
    # Handle the checkout.session.completed event
    elif event['type'] == 'checkout.session.completed':
        # import pdb ; pdb.set_trace()
        session = event['data']['object']
        # print("session: ", session)
        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        print('client_reference_id', client_reference_id)
        stripe_customer_id = session.get('customer')
        print('stripe_customer_id', stripe_customer_id)
        stripe_subscription_id = session.get('subscription')
        print('stripe_subscription_id', stripe_subscription_id)
        
        # Get the user and create a new StripeCustomer
        try:
          user = User.objects.get(id=client_reference_id)
          print('user', user)

          # Get Line Item To Get Product and Price Details
          line_items = stripe.checkout.Session.list_line_items(session.id)
          print("line items: ", line_items)
          price_id = line_items.data[0]['price']['id']
          price: stripe.Price = stripe.Price.retrieve(price_id)
          
          stripeCustomer = Subscription.objects.create(
            user = user,
            customer_key = stripe_customer_id,
            price_key = price_id,
            product_key = '',
            subscription_id = stripe_subscription_id
          ) 
          print(user.username + ' just subscribed.')
        except User.DoesNotExist:
          print('user not found just subscribed.')
           
    
    else:
      print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)



@api_view(['GET'])
def is_user_subscribed(request):
    current_month = timezone.now().month
    current_month_subs_count = Subscription.objects.filter(
       user = request.user, 
       date_created__month = current_month,
       isSubscribed = True
    ).count()

    return Response(
        data        = current_month_subs_count > 0, 
        status      = status.HTTP_200_OK
    )
    