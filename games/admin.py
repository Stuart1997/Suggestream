from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Genre, Game, Profile

# For each model, add it here so it can viewed in the admin GUI
admin.site.register(Genre)
admin.site.register(Game)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                  'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'fighting', 'first_person',
                  'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                  'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                  'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                  'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie']

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = [ProfileInline]
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
