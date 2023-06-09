from rest_framework import response, status
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, GenericAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Movie, TVShow, Director, Actor
from .serializers import MovieListSerializers, TVShowListSerializers, \
    MovieDetailSerializers, TVShowDetailSerializers, ActorSerializers, \
    DirectorSerializers, ActorDetailSerializers, DirectorDetailSerializers, CreateMovieReviewSerializer, \
    UpdateDestroyTVShowReviewSerializer, CreateTVShowReviewSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from ..users.models import MovieReview, TVShowReview


class MovieTVShowListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class_Movie = MovieListSerializers
    serializer_class_TVShow = TVShowListSerializers
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', '=rating', '=genre__name')

    def get_queryset_movie(self):
        return Movie.objects.all()

    def get_queryset_tv_show(self):
        return TVShow.objects.all()

    def list(self, request, *args, **kwargs):
        movie = self.serializer_class_Movie(self.get_queryset_movie(), many=True)
        tv_show = self.serializer_class_TVShow(self.get_queryset_tv_show(), many=True)
        return Response({
            "MOVIE": movie.data,
            "TV_SHOW": tv_show.data
        })


class MovieListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieListSerializers
    queryset = Movie.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', '=rating', '=genre__name')


class MovieDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieDetailSerializers
    queryset = Movie.objects.all()
    lookup_field = 'id'


class TVShowDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = TVShowDetailSerializers
    queryset = TVShow.objects.all()
    lookup_field = 'id'


class TVShowListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TVShowListSerializers
    queryset = TVShow.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', '=rating', '=genre__name')


class DirectorListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = DirectorSerializers
    queryset = Director.objects.all()

class DirectorDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = DirectorDetailSerializers
    queryset = Director.objects.all()
    lookup_field = 'id'


class ActorDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActorDetailSerializers
    queryset = Actor.objects.all()
    lookup_field = 'id'


class ActorListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActorSerializers
    queryset = Actor.objects.all()


class MovieReviewAPIView(ListCreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = CreateMovieReviewSerializer


class MovieReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateDestroyTVShowReviewSerializer
    queryset = MovieReview.objects.all()
    lookup_field = 'id'


class TVShowReviewAPIView(CreateAPIView):
    queryset = TVShowReview.objects.all()
    serializer_class = CreateTVShowReviewSerializer


class TVShowReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateDestroyTVShowReviewSerializer
    queryset = TVShowReview.objects.all()
    lookup_field = 'id'
