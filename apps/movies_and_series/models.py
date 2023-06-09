from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from apps.movies_and_series.utils import upload_instance, videos_uploaded


class Genre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now_add=False)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to=upload_instance,
                              blank=False, null=False)
    biography = models.CharField(verbose_name='Биография', max_length=512)

    # movie =
    # tv_shows =

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now_add=False)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to=upload_instance,
                              blank=False, null=False)
    biography = models.CharField(verbose_name='Биография', max_length=512)
    # movie =
    # tv_shows =

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    poster = models.ImageField(verbose_name='Постер',
                               upload_to=upload_instance,
                               blank=True, null=True)
    rating = models.FloatField(verbose_name='Рейтинг', default=10)
    content = models.FileField(verbose_name='Фильм', upload_to=videos_uploaded, null=True, blank=True,
                               validators=[FileExtensionValidator
                                           (allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    trailer = models.URLField(verbose_name='Трейлер')
    description = models.CharField(verbose_name='Описание', max_length=512)
    release_date = models.DateField(verbose_name='Дата выхода на сайте', null=True, blank=True)
    genre = models.ManyToManyField(verbose_name='Жанр',
                                   to='Genre')
    director = models.ManyToManyField(verbose_name='Режиссер',
                                      to='Director', related_name='movies')
    actor = models.ManyToManyField(verbose_name='Актер',
                                   to='Actor', related_name='movies')
    age_rating = models.IntegerField(verbose_name='Возрастной рейтинг')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.title}'


class TVShow(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    poster = models.ImageField(verbose_name='Постер',
                               upload_to=upload_instance,
                               blank=True, null=True)
    season = models.IntegerField(verbose_name='Номер сезона')
    rating = models.FloatField(verbose_name='Рейтинг', default=10)
    trailer = models.URLField(verbose_name='Трейлер')
    description = models.CharField(verbose_name='Описание', max_length=512)
    release_date = models.DateField(verbose_name='Дата выхода на сайте', null=True, blank=True)
    genre = models.ManyToManyField(verbose_name='Жанр',
                                   to='Genre')
    director = models.ManyToManyField(verbose_name='Режиссер',
                                      to='Director', related_name='tvshows')
    actor = models.ManyToManyField(verbose_name='Актер',
                                   to='Actor', related_name='tvshows')
    age_rating = models.IntegerField(verbose_name='Возрастной рейтинг')

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'

    def __str__(self):
        return f'{self.title} {self.season} сезон'


class Episode(models.Model):
    tv_show_title = models.ForeignKey(verbose_name='Сериал',
                                      to=TVShow,
                                      on_delete=models.CASCADE,
                                      related_name='episodes')
    number = models.IntegerField(verbose_name='Номер эпизода')
    poster = models.ImageField(verbose_name='Постер',
                               upload_to=upload_instance,
                               blank=False, null=False)
    trailer = models.FileField(verbose_name='Трайлер эпизода', upload_to=videos_uploaded, null=True, blank=True,
                               validators=[FileExtensionValidator
                                           (allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    title = models.CharField(verbose_name='Название', null=True, blank=True)
    content = models.FileField(verbose_name='Эпизод', upload_to=videos_uploaded, null=False,
                               validators=[FileExtensionValidator
                                           (allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    release_date = models.DateField(verbose_name='Дата выхода на сайте', auto_now_add=True)

    class Meta:
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'

    def __str__(self):
        return f'Сериал: {self.tv_show_title} Эпизод: {self.number}'




