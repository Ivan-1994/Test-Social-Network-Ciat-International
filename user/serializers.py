from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('username', 'password')
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user

        def to_representation(self, value):
            return {
                'id': value.id,
                'name': value.username,
            }


class UserLoginSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'password')

        def create(self, instance):
            user = authenticate(username=instance.username, password=instance.password)
            return {"token": user.auth_token.key}
