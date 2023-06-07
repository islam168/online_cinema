# Generated by Django 4.2.1 on 2023-06-07 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0015_remove_episode_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode_release_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения'),
        ),
    ]
