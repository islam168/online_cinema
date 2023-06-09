from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Movie, TVShow, Genre, Actor, Director, Episode
from apps.users.models import Purchase, User, MovieReview, TVShowReview
from .services import get_content
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class MovieReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MovieReview
        fields = ['user', 'rating', 'text']


class TVShowReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TVShowReview
        fields = ['user', 'rating', 'text']


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
        fields = ('title', 'poster', 'rating', 'description', 'release_date', 'genre', 'age_rating')


class MovieDetailSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    actor = ActorSerializers(many=True, read_only=True)
    director = DirectorSerializers(many=True, read_only=True)
    content = serializers.SerializerMethodField()
    moviereview = MovieReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'rating', 'poster', 'content', 'description', 'trailer',
                  'release_date', 'genre', 'director', 'actor', 'moviereview')

    def get_rating(self, obj):
        reviews = obj.moviereview.all()
        if reviews:
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            obj.rating = average_rating or 0
            obj.save()
            return obj.rating
        return 0

    def get_content(self, obj):
        age_rat = obj.age_rating
        user = self.context['request'].user
        if user.is_authenticated:
            purchase = Purchase.objects.filter(user=user.id).last()
            user_date_of_birth = User.objects.get(email=user).date_of_birth
            return get_content(user, purchase, user_date_of_birth, age_rat, obj)
        else:
            return 'Пожалуйста войдите в аккаунт'


class EpisodeSerializers(ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ['title', 'number', 'content', 'poster', 'trailer', 'release_date', 'tv_show_title']

    def get_content(self, obj):
        age_rat = TVShow.objects.get(id=obj.tv_show_title.id).age_rating
        user = self.context['request'].user
        if user.is_authenticated:
            purchase = Purchase.objects.filter(user=user.id).last()
            user_date_of_birth = User.objects.get(email=user).date_of_birth
            return get_content(user, purchase, user_date_of_birth, age_rat, obj)
        else:
            return 'Пожалуйста войдите в аккаунт'


class TVShowDetailSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    actor = ActorSerializers(many=True, read_only=True)
    director = DirectorSerializers(many=True, read_only=True)
    episodes = EpisodeSerializers(many=True, read_only=True)
    tvshowreview = TVShowReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = TVShow
        fields = ('id', 'title', 'poster', 'rating', 'season', 'episodes', 'description', 'trailer',
                  'release_date', 'genre', 'director', 'actor', 'age_rating', 'tvshowreview')

    def get_rating(self, obj):
        reviews = obj.tvshowreview.all()
        if reviews:
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            obj.rating = average_rating or 0
            obj.save()
            return obj.rating
        return 0


class TVShowListSerializers(ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)

    class Meta:
        model = TVShow
        fields = ('title', 'poster', 'rating', 'description', 'release_date', 'genre', 'age_rating')


class MovieSerializers(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'rating')


class TVShowSerializers(ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('title', 'genre', 'rating')


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


class CreateMovieReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieReview
        fields = ['user', 'rating', 'text', 'movie']


class CreateTVShowReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVShowReview
        fields = ['user', 'rating', 'text', 'tvshow']


class UpdateDestroyMovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = ['rating', 'text']


class UpdateDestroyTVShowReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = TVShowReview
        fields = ['rating', 'text']
