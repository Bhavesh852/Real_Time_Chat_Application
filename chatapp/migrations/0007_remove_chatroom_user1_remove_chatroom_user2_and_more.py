# Generated by Django 4.2.2 on 2023-07-01 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0006_rename_room_chatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='user2',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
