# Generated by Django 3.2.5 on 2021-08-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_id', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('reative_velocity', models.FloatField()),
                ('miss_distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Asteroid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_id', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=64)),
                ('absolute_magnitude_h', models.FloatField()),
                ('diameter', models.FloatField()),
                ('first_observed', models.DateField()),
                ('last_observed', models.DateField()),
                ('eccentricity', models.FloatField()),
                ('inclination', models.FloatField()),
                ('semi_major_axis', models.FloatField()),
                ('period', models.FloatField()),
                ('aphelion', models.FloatField()),
                ('perihelion', models.FloatField()),
            ],
        ),
    ]
