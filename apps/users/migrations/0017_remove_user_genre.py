# Generated by Django 4.2.1 on 2023-06-09 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_moviereview_text_alter_tvshowreview_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='genre',
        ),
    ]
