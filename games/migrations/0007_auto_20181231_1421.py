# Generated by Django 2.1.4 on 2018-12-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20181231_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='action',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='adventure',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='arcade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='building',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='cartoon',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='city_builder',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='class_based',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='twod',
            field=models.IntegerField(default=0),
        ),
    ]