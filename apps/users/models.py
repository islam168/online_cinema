from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework.authtoken.models import Token
from apps.movies_and_series.models import Genre, Movie, TVShow
from apps.users.managers import UserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Subscription(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.CharField(verbose_name='Описание', max_length=256)
    price = models.IntegerField(verbose_name='Цена')
    active = models.BooleanField(verbose_name='Активный', default=True)
    content_access_day = models.IntegerField(verbose_name='Через сколько дней доступен, контент', default=0)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.title}, Дней до открытия контента: {self.content_access_day}'


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    email = models.EmailField(verbose_name='Почта', unique=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now_add=True)
    genre = models.ManyToManyField(verbose_name='Подписка',
                                   to=Genre,
                                   related_name='users', blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Purchase(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь',
                             to='User',
                             on_delete=models.CASCADE,
                             related_name='purchases',
                             null=False)
    subscription = models.ForeignKey(verbose_name='Подписка',
                                     to='Subscription',
                                     on_delete=models.CASCADE,
                                     related_name='purchases',
                                     null=False)
    purchase_date = models.DateField(verbose_name='Дата покупки', default=timezone.now)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'Пользователь: {self.user}, Подписка: {self.subscription}, Дата покупки: {self.purchase_date}'


class MovieReview(models.Model):
    text = models.CharField(verbose_name='Текст отзыва', max_length=512)
    rating = models.IntegerField(verbose_name='Оценка',
                                 validators=[
                                     MinValueValidator(1, message='Оценка не менее 1'),
                                     MaxValueValidator(10, message='Оценка не выше 10')
                                 ], error_messages='Вы поставили неверную оценку, нужно поставить от 1 до 10')
    user = models.ForeignKey(verbose_name='Пользователь',
                             to=User,
                             on_delete=models.CASCADE,
                             related_name='moviereview')
    movie = models.ForeignKey(verbose_name='Фильм',
                              to=Movie,
                              on_delete=models.CASCADE,
                              related_name='moviereview')

    class Meta:
        verbose_name = 'Отзыв к фильму'
        verbose_name_plural = 'Отзывы к фильмам'

    def __str__(self):
        return f'Пользователь: {self.user}, Фильм: {self.movie}'


class TVShowReview(models.Model):
    text = models.CharField(verbose_name='Текст отзыва', max_length=512)
    rating = models.IntegerField(verbose_name='Оценка',
                                 validators=[
                                     MinValueValidator(1, message='Оценка не менее 1'),
                                     MaxValueValidator(10, message='Оценка не выше 10')
                                 ], error_messages='Вы поставили неверную оценку, нужно поставить от 1 до 10')
    user = models.ForeignKey(verbose_name='Пользователь',
                             to=User,
                             on_delete=models.CASCADE,
                             related_name='tvshowreview')
    tvshow = models.ForeignKey(verbose_name='Фильм',
                               to=TVShow,
                               on_delete=models.CASCADE,
                               related_name='tvshowreview')

    class Meta:
        verbose_name = 'Отзыв к сериалу'
        verbose_name_plural = 'Отзывы к сериалам'

    def __str__(self):
        return f'Пользователь: {self.user}, Фильм: {self.tvshow}'



