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
        fields = ['user', 'subscription']


class CreateMovieReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieReview
        fields = ['user', 'rating', 'text']


class CreateTVShowReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVShowReview
        fields = ['user', 'rating', 'text']

