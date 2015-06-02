# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
