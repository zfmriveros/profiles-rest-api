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
        extra_kwargs = {
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


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }

    # def create(self, validated_data):
    #     feed = models.ProfileFeedItem.objects.create(
    #         status_text=validated_data["status_text"],
    #         user_profile_id=1  # validated_data["user_profile"].id
    #     )
    #     return feed