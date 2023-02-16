from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}
