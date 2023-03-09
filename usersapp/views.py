from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from  django.shortcuts import redirect
from django.conf import settings

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

def email_Confirmation_optout(request):
    user_uuid = request.GET['uuid']
    user_token = request.GET['token']
    url_to_land = settings.EMAIL_CONFIRM_URL + "?uuid="+user_uuid+"&token="+user_token
    return redirect(url_to_land)