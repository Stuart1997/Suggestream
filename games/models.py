from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE, related_name='profile')
    twod = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    arcade = models.IntegerField(default=0)
    building = models.IntegerField(default=0)
    cartoon = models.IntegerField(default=0)
    city_builder = models.IntegerField(default=0)
    class_based = models.IntegerField(default=0)
    coop = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    competitive = models.IntegerField(default=0)
    crafting = models.IntegerField(default=0)
    destruction = models.IntegerField(default=0)
    difficult = models.IntegerField(default=0)
    driving = models.IntegerField(default=0)
    dystopian = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    fighting = models.IntegerField(default=0)
    first_person = models.IntegerField(default=0)
    fps = models.IntegerField(default=0)
    free_to_play = models.IntegerField(default=0)
    futuristic = models.IntegerField(default=0)
    historical = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    indie = models.IntegerField(default=0)
    magic = models.IntegerField(default=0)
    medieval = models.IntegerField(default=0)
    military = models.IntegerField(default=0)
    moba = models.IntegerField(default=0)
    multiplayer = models.IntegerField(default=0)
    open_world = models.IntegerField(default=0)
    post_apocalyptic = models.IntegerField(default=0)
    procedural_generation = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)
    racing = models.IntegerField(default=0)
    rpg = models.IntegerField(default=0)
    rts = models.IntegerField(default=0)
    sandbox = models.IntegerField(default=0)
    scifi = models.IntegerField(default=0)
    shooter = models.IntegerField(default=0)
    side_scroller = models.IntegerField(default=0)
    singleplayer = models.IntegerField(default=0)
    soccer = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    sports = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    third_person = models.IntegerField(default=0)
    tower_defence = models.IntegerField(default=0)
    vr = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    zombie = models.IntegerField(default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


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
    clip = models.CharField(max_length=300, default="https://clips.twitch.tv/embed?clip=")
    streams = models.CharField(max_length=300, null=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
