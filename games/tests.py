from django.test import TestCase

from django.test import TestCase
from .models import Game
from .views import GamesPageByGenre
from datetime import datetime


class TestGameModel(TestCase):
    def setUp(self):
        Game.objects.create(
            name="Metro Exodus",
            description="The third Metro game",
            developer="4A Games",
            release_date=datetime.now(),
            metacritic=100,
            image="www.image.com",
            steam="www.steam.com",
            clip="www.clip.com",
            streams="www.stream.com"
        )

    def test_game_is_created(self):
        """A new game is created and its name is printed"""
        metro_exodus = Game.objects.get(name="Metro Exodus")

        self.assertEqual(metro_exodus.__str__(), "Metro Exodus")


class TestGameView(TestCase):
    def setUp(self):
        Game.objects.create(
            name="Metro Exodus",
            description="The third Metro game",
            developer="4A Games",
            release_date=datetime.now(),
            metacritic=100,
            image="www.image.com",
            steam="www.steam.com",
            clip="www.clip.com",
            streams="www.stream.com"
        )
        Game.objects.create(
            name="Tom Clancy's Rainbow Six Siege",
            description="Latest R6 game",
            developer="Ubisoft",
            release_date=datetime.now(),
            metacritic=90,
            image="www.image.com",
            steam="www.steam.com",
            clip="www.clip.com",
            streams="www.stream.com"
        )

    def test_queryset(self):
        """A new game is created and its name is printed"""
        #metro_exodus = Game.objects.get(name="Metro Exodus")

        #self.assertEqual(metro_exodus.__str__(), "Metro Exodus")
