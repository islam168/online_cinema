# Generated by Django 4.2.1 on 2023-06-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_subscription_content_access_day_alter_user_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='duration',
            field=models.IntegerField(default=30, verbose_name='Длительность'),
        ),
    ]
