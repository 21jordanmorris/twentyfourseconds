# Generated by Django 3.0.5 on 2020-04-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default='slug_game', unique=True),
            preserve_default=False,
        ),
    ]
