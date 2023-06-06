from rest_framework.generics import (
    ListAPIView, RetrieveAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Movie, TVShow, Director, Actor
from .serializers import MovieListSerializers, TVShowListSerializers, \
    MovieDetailSerializers, TVShowDetailSerializers, ActorSerializers, \
    DirectorSerializers, ActorDetailSerializers, DirectorDetailSerializers


class MovieTVShowListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class_Movie = MovieListSerializers
    serializer_class_TVShow = TVShowListSerializers

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


class MovieDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    lookup_field = 'id'
    serializer_class = MovieDetailSerializers


class TVShowDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = TVShowDetailSerializers
    queryset = TVShow.objects.all()
    lookup_field = 'id'


class TVShowListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TVShowListSerializers
    queryset = TVShow.objects.all()


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
