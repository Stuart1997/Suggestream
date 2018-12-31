# Generated by Django 2.1.4 on 2018-12-31 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_profile_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twod', models.IntegerField()),
                ('action', models.IntegerField()),
                ('adventure', models.IntegerField()),
                ('arcade', models.IntegerField()),
                ('building', models.IntegerField()),
                ('cartoon', models.IntegerField()),
                ('city_builder', models.IntegerField()),
                ('class_based', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Profile'),
        ),
    ]
