from django.contrib import admin
from .models import Genre, Game

# For each model, add it here so it can viewed in the admin GUI
admin.site.register(Genre)
admin.site.register(Game)
