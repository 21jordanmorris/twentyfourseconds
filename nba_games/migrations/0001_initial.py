# Generated by Django 3.0.4 on 2020-04-06 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('home_team', models.CharField(max_length=3)),
                ('visitor_team', models.CharField(max_length=3)),
                ('home_score', models.IntegerField(blank=True, null=True)),
                ('visitor_score', models.IntegerField(blank=True, null=True)),
                ('home_probability', models.FloatField()),
                ('visitor_probability', models.FloatField()),
            ],
        ),
    ]