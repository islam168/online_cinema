from django.urls import path
from .views import (
    MovieTVShowListAPIView, MovieListAPIView, TVShowListAPIView, MovieDetailAPIView,
    TVShowDetailAPIView, DirectorListAPIView, DirectorDetailAPIView, ActorListAPIView, ActorDetailAPIView,
    MovieReviewAPIView, MovieReviewDetailAPIView, TVShowReviewAPIView, TVShowReviewDetailAPIView
)

urlpatterns = [
    path('', MovieTVShowListAPIView.as_view(), name='content_list'),
    path('movies', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<int:id>', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('tvshows', TVShowListAPIView.as_view(), name='tv_show_list'),
    path('tvshow/<int:id>', TVShowDetailAPIView.as_view(), name='tv_show_detail'),
    path('actors', ActorListAPIView.as_view(), name='actor_list'),
    path('actors/<int:id>', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('directors', DirectorListAPIView.as_view(), name='director_list'),
    path('directors/<int:id>', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('moviereview', MovieReviewAPIView.as_view(), name='create_movie_review'),
    path('moviereview/<int:id>', MovieReviewDetailAPIView.as_view(), name='movie_detail'),
    path('tvshowreview', TVShowReviewAPIView.as_view(), name='create_tv_show_review'),
    path('tvshowreview/<int:id>', TVShowReviewDetailAPIView.as_view(), name='tv_show_detail'),

]