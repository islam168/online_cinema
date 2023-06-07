from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Movie, TVShow, Genre, Actor, Director, Episode
from apps.users.models import Purchase
from .services import get_content


class GenreSerializers(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class ActorSerializers(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']


class DirectorSerializers(ModelSerializer):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name']


class MovieListSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'poster', 'description', 'release_date', 'genre', 'age_rating')


class MovieDetailSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    actor = ActorSerializers(many=True, read_only=True)
    director = DirectorSerializers(many=True, read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'poster', 'content', 'description', 'trailer',
                  'release_date', 'genre', 'director', 'actor', 'age_rating')

    def get_content(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            purchase = list(Purchase.objects.filter(user=user.id))
            return get_content(user, purchase, obj)
        else:
            return 'Пожалуйста войдите в аккаунт'


class EpisodeSerializers(ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ['title', 'number', 'content', 'poster', 'trailer', 'release_date']

    def get_content(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            purchase = Purchase.objects.filter(user=user.id).last()
            return get_content(user, purchase, obj)
        else:
            return 'Пожалуйста войдите в аккаунт'


class TVShowDetailSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    actor = ActorSerializers(many=True, read_only=True)
    director = DirectorSerializers(many=True, read_only=True)
    episodes = EpisodeSerializers(many=True, read_only=True)

    class Meta:
        model = TVShow
        fields = ('title', 'poster', 'season', 'episodes', 'description', 'trailer',
                  'release_date', 'genre', 'director', 'actor', 'age_rating')


class TVShowListSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)

    class Meta:
        model = TVShow
        fields = ('title', 'poster', 'description', 'release_date', 'genre', 'age_rating')


class MovieSerializers(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class TVShowSerializers(ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('title',)


class ActorDetailSerializers(ModelSerializer):
    movies = TVShowSerializers(many=True, read_only=True)
    tvshows = MovieSerializers(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth', 'photo', 'movies', 'tvshows', 'biography']


class DirectorDetailSerializers(ModelSerializer):
    movies = TVShowSerializers(many=True, read_only=True)
    tvshows = MovieSerializers(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth', 'photo', 'movies', 'tvshows', 'biography']
