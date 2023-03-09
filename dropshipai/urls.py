from django.contrib import admin
from django.urls import path, include
from usersapp import views as user_views
from rest_framework_nested import routers
from productapp import views as productViews
from paymentapp import views as paymentViews

router = routers.DefaultRouter()
router.register('users', user_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('product/ping/', productViews.ping, name="product_ping"),
    path('product/', productViews.getRandomProduct, name="product"),
    path('external/email-confirmation/',user_views.email_Confirmation_optout, name="email-confirmation-out"),
    path('payment/checkout/create-checkout-session/' , paymentViews.CreateCheckoutSession.as_view()), 
    path('payment/webhook/' , paymentViews.WebHook.as_view()), 
]
