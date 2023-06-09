from rest_framework import serializers
from rest_framework.fields import EmailField, CharField

from apps.users.models import User, Purchase, Subscription, MovieReview, TVShowReview
from apps.movies_and_series.serializers import GenreSerializers


class UserSerializer(serializers.ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'date_of_birth', 'genre')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'date_of_birth', 'genre')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserChangePasswordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ('user', 'password')

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'genre')


class UserAuthSerializer(serializers.Serializer):
    email = EmailField(required=True)
    password = CharField(max_length=128, required=True)


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'title', 'description', 'price', 'content_access_day', 'duration']


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'subscription']
