# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_users(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    CustomUser = apps.get_model("users", "CustomUser")

    superuser = CustomUser(username='admin', email='admin@telmediq.com',
                           first_name='Admin', last_name='User', is_staff=True,
                           is_superuser=True, password='pbkdf2_sha256$15000$ahV43c657dY9$UOntKzDAOmjMa0XicpnBN3f1Y6TU/xPi4GLG7L+maQc=')

    superuser.save()

def delete_users(apps, schema_editor):
    CustomUser = apps.get_model("users", "CustomUser")

    CustomUser.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, delete_users),
    ]
