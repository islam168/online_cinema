from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Movie, TVShow, Genre, Actor, Director, Episode


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
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'poster', 'movie', 'description', 'trailer',
                  'release_date', 'genre', 'director', 'actor', 'age_rating')

    def get_movie(self, obj):
        if self.context['request'].user.is_authenticated:
            return f'http://127.0.0.1:8000{obj.movie.url}'
        else:
            return 'Please login to view the movie.'


class EpisodeSerializers(ModelSerializer):
    episode = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ['title', 'number', 'episode']


    def get_episode(self, obj):
        if self.context['request'].user.is_authenticated:
            return f'http://127.0.0.1:8000{obj.episode.url}'
        else:
            return 'Please login to view the episode.'


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

