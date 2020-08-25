from rest_framework import serializers
from .models import User_info, account
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = account
        # fields = '__all__'
        fields = ['email', 'otp', 'password', 'is_verified', 'is_active']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(AccountSerializer, self).create(validated_data)

