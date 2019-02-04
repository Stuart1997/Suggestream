from SuggestreamProject import settings
from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


GENRE_CHOICES = [
    ('twod', '2D'), ('action', 'Action'), ('adventure', 'Adventure'), ('arcade', 'Arcade'), ('building', 'Building'),
    ('cartoon', 'Cartoon'), ('city_builder', 'City Builder'), ('class_based', 'Class-based'), ('coop', 'Co-op'),
    ('comedy', 'Comedy'), ('competitive', 'Competitive'), ('crafting', 'Crafting'), ('destruction', 'Destruction'),
    ('difficult', 'Difficult'), ('driving', 'Driving'), ('dystopian', 'Dystopian'), ('fantasy', 'Fantasy'),
    ('first_person', 'First Person'), ('fps', 'FPS'), ('free_to_play', 'Free To Play'), ('futuristic', 'Futuristic'),
    ('historical', 'Historical'), ('horror', 'Horror'), ('indie', 'Indie'), ('magic', 'Magic'), ('medieval', 'Medieval'),
    ('military', 'Military'), ('moba', 'MOBA'), ('multiplayer', 'Multiplayer'), ('open_world', 'Open World'),
    ('post_apocalyptic', 'Post-apocalyptic'), ('procedural_generation', 'Procedural Generation'), ('puzzle', 'Puzzle'),
    ('racing', 'Racing'), ('rpg', 'RPG'), ('rts', 'RTS'), ('sandbox', 'Sandbox'), ('scifi', 'Sci-fi'), ('shooter', 'Shooter'),
    ('side_scroller', 'Side Scroller'), ('singleplayer', 'Singleplayer'), ('soccer', 'Soccer'), ('space', 'Space'),
    ('sports', 'Sports'), ('stealth', 'Stealth'), ('strategy', 'Strategy'), ('survival', 'Survival'),
    ('third_person', 'Third Person'), ('tower_defence', 'Tower Defence'), ('vr', 'VR'), ('war', 'War'), ('zombie', 'Zombie')
]


#Create a class which inherits from Django's UserCreationForm class and add fields necessary for my users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit)
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user',
                  'twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                  'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'fighting', 'first_person',
                  'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                  'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                  'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                  'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie')
