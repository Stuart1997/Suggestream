# Generated by Django 2.1.4 on 2019-01-23 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_auto_20181231_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='action',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adventure',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='arcade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='building',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cartoon',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city_builder',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class_based',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twod',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
