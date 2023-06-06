from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html

from apps.movies_and_series.models import Genre, Director, Actor, Movie, TVShow, Episode

AdminSite.site_header = 'Администрирование ONLINE CINEMA'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_poster', 'get_movie', 'trailer', 'description',
                    'release_date', 'get_genre', 'get_director', 'get_actor', 'age_rating')
    search_fields = ['title']

    def get_poster(self, obj):
        return format_html(f'<img src="{obj.poster.url}" '
                           f'width="100" height="150" />')

    get_poster.short_description = 'Постер'

    def get_movie(self, obj):
        print(obj.movie)
        if not obj.movie:
            return "Фильм ещё не загружен"
        else:
            return format_html(f'<video width="250" height="150" controls="controls">'
                               f'<source src="/media/{obj.movie}" type="video/mp4;">'
                               f'</video>')

    get_movie.short_description = 'Фильм'

    def get_director(self, obj):
        return ', '.join([str(director) for director in obj.director.all()])

    get_director.short_description = 'Режиссер'

    def get_genre(self, obj):
        return ', '.join([str(genre) for genre in obj.genre.all()])

    get_genre.short_description = 'Жанр'

    def get_actor(self, obj):
        return ', '.join([str(actor) for actor in obj.actor.all()])

    get_actor.short_description = 'Актёр'


@admin.register(TVShow)
class TVShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_poster', 'season', 'trailer', 'description',
                    'release_date', 'get_genre', 'get_director', 'get_actor', 'age_rating')
    search_fields = ['title']

    def get_poster(self, obj):
        return format_html(f'<img src="{obj.poster.url}" '
                           f'width="100" height="150" />')

    get_poster.short_description = 'Постер'

    def get_director(self, obj):
        return ', '.join([str(director) for director in obj.director.all()])

    get_director.short_description = 'Режиссер'

    def get_genre(self, obj):
        return ', '.join([str(genre) for genre in obj.genre.all()])

    get_genre.short_description = 'Жанр'

    def get_actor(self, obj):
        return ', '.join([str(actor) for actor in obj.actor.all()])

    get_actor.short_description = 'Актёр'


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('tv_show_title', 'number', 'title', 'get_episode')
    search_fields = ['tv_show_title']

    def get_episode(self, obj):
        return format_html(f'<video width="250" height="150" controls="controls">'
                           f'<source src="/media/{obj.episode}" type="video/mp4;">'
                           f'</video>')

    get_episode.short_description = 'Эпизод'

    def get_director(self, obj):
        return ', '.join([str(director) for director in obj.director.all()])

    get_director.short_description = 'Режиссер'

    def get_genre(self, obj):
        return ', '.join([str(genre) for genre in obj.genre.all()])

    get_genre.short_description = 'Жанр'

    def get_actor(self, obj):
        return ', '.join([str(actor) for actor in obj.actor.all()])

    get_actor.short_description = 'Актёр'
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)

