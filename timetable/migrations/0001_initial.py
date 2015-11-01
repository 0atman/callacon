# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('postcode', models.CharField(max_length=10)),
                ('game_master', models.ForeignKey(related_name='games_running', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='games_playing_in', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
