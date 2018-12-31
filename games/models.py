from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

#https://www.youtube.com/watch?v=iJCbYMgUDW8  USERFOREIGNKEY MIDDLEWARE

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twod = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    arcade = models.IntegerField(default=0)
    building = models.IntegerField(default=0)
    cartoon = models.IntegerField(default=0)
    city_builder = models.IntegerField(default=0)
    class_based = models.IntegerField(default=0)
    #date_of_birth = models.DateField(default=date.today)

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    metacritic = models.IntegerField()
    image = models.CharField(max_length=1000, default="https://steamstore-a.akamaihd.net/public/shared/images/responsive/share_steam_logo.png")
    steam = models.CharField(max_length=1000, default="https://store.steampowered.com/")
    genres = models.ManyToManyField(Genre)

    # Whenever a game is added, it'll give it a pk, and go to detail view
    #def get_absolute_url(self):
    #    return reverse('game:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


'''
class GUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
'''

'''
class UserPreferences(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    twod = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    arcade = models.IntegerField()
    building = models.IntegerField()
    cartoon = models.IntegerField()
    city_builder = models.IntegerField()
    class_based = models.IntegerField()
'''

#game = Game.objects.get(id=2)
#for genre in game.genres.all().order_by('pref_count')[0:5]:
#    pass