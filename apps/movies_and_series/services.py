#
# from rest_framework.response import Response
# from .models import Movie, TVShow
# from .serializers import MovieListSerializers, TVShowListSerializers
#
#
# def movies_and_tv_shows():
#     serializer_class_Movie = MovieListSerializers
#     serializer_class_TVShow = TVShowListSerializers
#
#     def get_queryset_Movie(self):
#         return Movie.objects.all()
#
#     def get_queryset_TVShows(self):
#         return TVShow.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         movie = self.serializer_class_Movie(self.get_queryset_Movie(), many=True)
#         tvshow = self.serializer_class_TVShow(self.get_queryset_TVShows(), many=True)
#         return Response({
#             "MOVIE": movie.data,
#             "TVSHOW": tvshow.data
#         })
