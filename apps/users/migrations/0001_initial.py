# Generated by Django 4.2.1 on 2023-06-05 00:45

import apps.users.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movies_and_series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('genre', models.ManyToManyField(related_name='users', to='movies_and_series.genre', verbose_name='Подписка')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.subscription', verbose_name='Подписка')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', apps.users.managers.UserManager()),
            ],
        ),
    ]