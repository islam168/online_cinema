# Generated by Django 4.2.1 on 2023-06-07 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0018_alter_episode_episode_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='episode',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='episode_release_date',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie',
            new_name='content',
        ),
    ]
