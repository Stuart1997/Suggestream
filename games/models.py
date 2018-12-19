from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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


class GUserPref(models.Model):
    user = models.ForeignKey(GUser, on_delete=models.CASCADE)
    pref_count = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name='genres')
'''

#game = Game.objects.get(id=2)
#for genre in game.genres.all().order_by('pref_count')[0:5]:
#    pass