from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, GenericAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Movie, TVShow, Director, Actor
from .serializers import MovieListSerializers, TVShowListSerializers, \
    MovieDetailSerializers, TVShowDetailSerializers, ActorSerializers, \
    DirectorSerializers, ActorDetailSerializers, DirectorDetailSerializers
from rest_framework import mixins


class ListCreateRetrieveUpdateDestroyAPIView(mixins.ListModelMixin,
                                             mixins.CreateModelMixin,
                                             mixins.UpdateModelMixin,
                                             mixins.DestroyModelMixin,
                                             GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


# ListCreateRetrieveUpdateDestroyAPIView
class MovieDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers
    lookup_field = 'id'

