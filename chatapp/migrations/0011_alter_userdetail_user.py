# Generated by Django 4.2.2 on 2023-07-01 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0010_remove_userdetail_age_remove_userdetail_interest_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]