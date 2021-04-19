from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """"Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserprofileSerializer(serializers.ModelSerializer):
    """
    Serialized a user profile object
    """
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwards = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """
        Creates and return a new user
        :param validated_data:
        :return:
        """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """
        Handle updating user account
        :param instance:
        :param validated_data:
        :return:
        """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)