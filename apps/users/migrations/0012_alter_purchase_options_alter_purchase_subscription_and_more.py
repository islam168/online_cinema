# Generated by Django 4.2.1 on 2023-06-05 16:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0002_actor_director_tvshow_movie_episode_director_movie_and_more'),
        ('users', '0011_alter_purchase_options_purchase_purchase_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Покупка', 'verbose_name_plural': 'Покупки'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='users.subscription', verbose_name='Подписка'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='TVShowReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(error_messages='Вы поставили неверную оценку, нужно поставить от 1 до 10', validators=[django.core.validators.MinValueValidator(1, message='Оценка не менее 1'), django.core.validators.MaxValueValidator(10, message='Оценка не выше 10')], verbose_name='Оценка')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvshowreview', to='movies_and_series.tvshow', verbose_name='Фильм')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvshowreview', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(error_messages='Вы поставили неверную оценку, нужно поставить от 1 до 10', validators=[django.core.validators.MinValueValidator(1, message='Оценка не менее 1'), django.core.validators.MaxValueValidator(10, message='Оценка не выше 10')], verbose_name='Оценка')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviereview', to='movies_and_series.movie', verbose_name='Фильм')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviereview', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
