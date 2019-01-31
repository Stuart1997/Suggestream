from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Game, Genre, Profile
from .forms import UserRegisterForm, ProfileForm
from django.forms.models import model_to_dict
from operator import itemgetter
from itertools import chain
import random

# Displays all results as a listview on the index page
def home(request):
    return render(request, 'games/index.html')


class GenreSearch(generic.ListView):
    template_name = 'games/genresearch.html'
    context_object_name = 'genre_list'

    def get_queryset(self):
        return Genre.objects.order_by("name")


class TitleSearch(generic.ListView):
    template_name = 'games/titlesearch.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.order_by("name")


class GamesPageAlphabetically(generic.ListView):
    template_name = 'games/allgames.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.order_by("name")


class GamesPageByRating(generic.ListView):
    template_name = 'games/allgames.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.order_by("-metacritic")


class GamesPageByGenre(generic.ListView):
    template_name = 'games/genresearchresults.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        #Grabs the genre name and user's ID from the GenreSearch URL query, these are used to query all games with
        #the selected genre, and to then grab the profile of the currently logged in user to increment their preferences
        genre_name = self.request.GET.get("genre")
        user_id = self.request.GET.get("userid")

        #If the user isn't logged in then their preferences can't be updated
        if user_id != None:
            user = Profile.objects.get(user_id=user_id)
            print("-----------------------------------")
            print("User = ", user)
            print("Genre = ", genre_name)
            print("User ID = ", user_id)
            print()

            #Replaces spaces with underscores as genres like "Class based" are "class_based" in preferences
            if " " in genre_name:
                edited = genre_name.replace(" ", "_")
                genreToUpdate = edited.lower()
            else:
                edited = genre_name
                genreToUpdate = edited.lower()

            print("Genre to update lowercase: ", genreToUpdate)

            #Discrepencies to the correction above are all handled here to ensure the game genre and
            #user profile genre preferences match
            if genreToUpdate == "2d":
                genreToUpdate = "twod"
            elif genreToUpdate == "class-based":
                genreToUpdate = "class_based"
            elif genreToUpdate == "co-op":
                genreToUpdate = "coop"
            elif genreToUpdate == "post-apocalyptic":
                genreToUpdate = "post_apocalyptic"
            elif genreToUpdate == "sci-fi":
                genreToUpdate = "scifi"

            print("Genre to update after validation: ", genreToUpdate)

            #Dynamically retrieves the user's preference value of the queried genre
            retrieve = getattr(user, genreToUpdate)
            print("Profile value: ", genreToUpdate, " = ", retrieve)

            #Sets this queried genre to +1 of what it already was to learn they've shown interest in this genre
            setattr(user, genreToUpdate, retrieve + 1)

            #Save this change in the database
            user.save()
            print("User's ", genreToUpdate, " after incrementing = ", getattr(user, genreToUpdate))

        #Once either the preferences have been updated or if there is no user ID, retrieve all games that match the genre they selected
        print("GENRE NAME = ", genre_name)
        return Game.objects.filter(genres__name=str(genre_name))

    #TODO FOR MULTI GENRE SEARCH - return Game.objects.filter(genres__name=str('Action')).filter(genres__name=str('Side Scroller'))


class Recommended(generic.ListView):
    template_name = 'games/recommended.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        user_id = self.request.GET.get("userid")

        if user_id != None:
            user = Profile.objects.get(user_id=user_id)

            listOfGenres = ['twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                            'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'first_person',
                            'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                            'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                            'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                            'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie']

            listOfPreferences = []
            for genre in listOfGenres: listOfPreferences.append(getattr(user, genre))

            userPreferences = list(zip(listOfGenres, listOfPreferences))
            userPreferences.sort(key=itemgetter(1), reverse=True)
            print("Top 3 genres:", userPreferences[0], userPreferences[1], userPreferences[2])

            listOfValidatedGenres = []

            #For their top 3 genres, ensure the case and spacing is correctly formatted
            for genre in range(3):
                currentGenre = userPreferences[genre][0]

                if "_" in currentGenre:
                    if currentGenre == "post_apocalyptic":          currentGenre = "Post-apocalyptic"
                    elif currentGenre == "city_builder":            currentGenre = "City Builder"
                    elif currentGenre == "free_to_play":            currentGenre = "Free To Play"
                    elif currentGenre == "class_based":             currentGenre = "Class-based"
                    elif currentGenre == "first_person":            currentGenre = "First Person"
                    elif currentGenre == "open_world":              currentGenre = "Open World"
                    elif currentGenre == "procedural_generation":   currentGenre = "Procedural Generation"
                    elif currentGenre == "side_scroller":           currentGenre = "Side Scroller"
                    elif currentGenre == "third_person":            currentGenre = "Third Person"
                    elif currentGenre == "tower_defence":           currentGenre = "Tower Defence"

                elif currentGenre == "twod":    currentGenre = "2D"
                elif currentGenre == "scifi":   currentGenre = "Sci-fi"
                elif currentGenre == "coop":    currentGenre = "Co-op"
                elif currentGenre == "fps" or currentGenre == "rts" or currentGenre == "vr" or currentGenre == "rpg" or currentGenre == "moba":
                    currentGenre = userPreferences[genre][0].upper()

                else:
                    capitalised = currentGenre[0:].capitalize()
                    currentGenre = capitalised

                #Add the corrected genre name to the list at the end of each loop
                listOfValidatedGenres.append(currentGenre)

            print("Top genre name and value:", userPreferences[0][0])
            print("TOP 3: ", listOfValidatedGenres)

            #Return all games that match the top 3 genres, with no duplicates
            return Game.objects.filter(genres__name__in=[listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2]]).distinct()

            #TODO Order by ? is bad practice apparently, use this https://stackoverflow.com/questions/1731346/how-to-get-two-random-records-with-django#6405601

    def get_context_data(self, **kwargs):
        context = super(Recommended, self).get_context_data(**kwargs)

        user_id = self.request.GET.get("userid")

        listOfValidatedGenres = []

        if user_id != None:
            user = Profile.objects.get(user_id=user_id)

            listOfGenres = ['twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                            'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'first_person',
                            'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                            'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                            'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                            'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie']

            listOfPreferences = []
            for genre in listOfGenres: listOfPreferences.append(getattr(user, genre))

            userPreferences = list(zip(listOfGenres, listOfPreferences))
            userPreferences.sort(key=itemgetter(1), reverse=True)
            print("Top 3 genres:", userPreferences[0], userPreferences[1], userPreferences[2])


            # For their top 3 genres, ensure the case and spacing is correctly formatted
            for genre in range(3):
                currentGenre = userPreferences[genre][0]

                if "_" in currentGenre:
                    if currentGenre == "post_apocalyptic":
                        currentGenre = "Post-apocalyptic"
                    elif currentGenre == "city_builder":
                        currentGenre = "City Builder"
                    elif currentGenre == "free_to_play":
                        currentGenre = "Free To Play"
                    elif currentGenre == "class_based":
                        currentGenre = "Class-based"
                    elif currentGenre == "first_person":
                        currentGenre = "First Person"
                    elif currentGenre == "open_world":
                        currentGenre = "Open World"
                    elif currentGenre == "procedural_generation":
                        currentGenre = "Procedural Generation"
                    elif currentGenre == "side_scroller":
                        currentGenre = "Side Scroller"
                    elif currentGenre == "third_person":
                        currentGenre = "Third Person"
                    elif currentGenre == "tower_defence":
                        currentGenre = "Tower Defence"

                elif currentGenre == "twod":
                    currentGenre = "2D"
                elif currentGenre == "scifi":
                    currentGenre = "Sci-fi"
                elif currentGenre == "coop":
                    currentGenre = "Co-op"
                elif currentGenre == "fps" or currentGenre == "rts" or currentGenre == "vr" or currentGenre == "rpg" or currentGenre == "moba":
                    currentGenre = userPreferences[genre][0].upper()

                else:
                    capitalised = currentGenre[0:].capitalize()
                    currentGenre = capitalised

                # Add the corrected genre name to the list at the end of each loop
                listOfValidatedGenres.append(currentGenre)

        print(listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2])
        context['recommended_genres'] = Genre.objects.all().filter(name__in=[listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2]])
        return context

# Displays all information about a single game on a detail page
class DetailPage(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profileform = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.profile.save()
            messages.success(request, 'Account created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    args = {'form': form}
    return render(request, 'games/register.html', args)


#Prevents this view from being accessed if the user isn't logged in
@login_required
def profile(request):
    preferences = model_to_dict(request.user.profile)
    return render(request, 'games/profile.html', {'preferences': preferences})

#If the url doesn't have anything after the slash, redirect them to the login page
def login_redirect(request):
    return redirect('games:login')


def login_prompt(request):
    return redirect('games:login')
