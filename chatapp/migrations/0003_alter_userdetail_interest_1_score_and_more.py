# Generated by Django 4.2.2 on 2023-06-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_alter_userdetail_interest_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='interest_1_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest_2_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest_3_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest_4_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest_5_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest_6_score',
            field=models.IntegerField(blank=True),
        ),
    ]