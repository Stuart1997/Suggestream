# Generated by Django 2.1.4 on 2019-02-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_auto_20190211_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='clip',
            field=models.CharField(default='https://clips.twitch.tv/embed?clip=', max_length=300),
        ),
    ]
