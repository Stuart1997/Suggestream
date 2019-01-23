from SuggestreamProject import settings
from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


BIRTH_YEAR_CHOICES = (2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991,
                      1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981,
                      1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971,
                      1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961,
                      1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951,
                      1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941,
                      1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931,
                      1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921,
                      1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911,
                      1910, 1909, 1908, 1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900)


#Create a class which inherits from Django's UserCreationForm class and add fields necessary for my users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


    #8 MINUTES INTO PART 16 OF MAX GOODRIDGE VIDEOS - clean data
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit)
        return user


#http://www.re-cycledair.com/extending-djangos-model-save-method

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


#https://stackoverflow.com/questions/3523745/best-way-to-do-register-a-user-in-django/17005485#17005485
