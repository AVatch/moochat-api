# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='account',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_picture_url',
            field=models.URLField(default=b'http://placehold.it/350x350', blank=True),
        ),
    ]
