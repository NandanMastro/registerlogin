from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from . import models
from . import serializers


class UsersViewset(viewsets.ModelViewSet):
    queryset = models.User_info.objects.all()
    serializer_class = serializers.UserSerializer


class AccountViewset(viewsets.ModelViewSet):
    queryset = models.account.objects.all()
    serializer_class = serializers.AccountSerializer
