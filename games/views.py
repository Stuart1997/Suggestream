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


class SelectFavouriteGenres(generic.ListView):
    template_name = 'games/favourites.html'
    context_object_name = 'genre_list'

    def get_queryset(self):
        return Genre.objects.order_by("name")


class SubmitFavourites(generic.ListView):
    template_name = 'games/thankyou.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        #Grabs the genre name and user's ID from the GenreSearch URL query, these are used to query all games with
        #the selected genre, and to then grab the profile of the currently logged in user to increment their preferences
        genre1_name = self.request.GET.get("genre1")
        genre2_name = self.request.GET.get("genre2")
        genre3_name = self.request.GET.get("genre3")
        user_id = self.request.GET.get("userid")

        #If the user isn't logged in then their preferences can't be updated
        if user_id != "None":
            user = Profile.objects.get(user_id=user_id)
            print("-----------------------------------")
            print("User = ", user)
            print("Genre1 = ", genre1_name)
            print("Genre2 = ", genre2_name)
            print("Genre3 = ", genre3_name)
            print("User ID = ", user_id)
            print()

            #Replaces spaces with underscores as genres like "Class based" are "class_based" in preferences
            if " " in genre1_name:
                edited = genre1_name.replace(" ", "_")
                genre1ToUpdate = edited.lower()
            else:
                edited = genre1_name
                genre1ToUpdate = edited.lower()

            print("Genre1 to update lowercase: ", genre1ToUpdate)

            #Discrepencies to the correction above are all handled here to ensure the game genre and
            #user profile genre preferences match
            if genre1ToUpdate == "2d":                  genre1ToUpdate = "twod"
            elif genre1ToUpdate == "class-based":       genre1ToUpdate = "class_based"
            elif genre1ToUpdate == "co-op":             genre1ToUpdate = "coop"
            elif genre1ToUpdate == "post-apocalyptic":  genre1ToUpdate = "post_apocalyptic"
            elif genre1ToUpdate == "sci-fi":            genre1ToUpdate = "scifi"


            #Second genre
            if " " in genre2_name:
                edited = genre2_name.replace(" ", "_")
                genre2ToUpdate = edited.lower()
            else:
                edited = genre2_name
                genre2ToUpdate = edited.lower()

            print("Genre2 to update lowercase: ", genre2ToUpdate)

            # Discrepencies to the correction above are all handled here to ensure the game genre and
            # user profile genre preferences match
            if genre2ToUpdate == "2d":                  genre2ToUpdate = "twod"
            elif genre2ToUpdate == "class-based":       genre2ToUpdate = "class_based"
            elif genre2ToUpdate == "co-op":             genre2ToUpdate = "coop"
            elif genre2ToUpdate == "post-apocalyptic":  genre2ToUpdate = "post_apocalyptic"
            elif genre2ToUpdate == "sci-fi":            genre2ToUpdate = "scifi"

            # Third genre
            if " " in genre3_name:
                edited = genre3_name.replace(" ", "_")
                genre3ToUpdate = edited.lower()
            else:
                edited = genre3_name
                genre3ToUpdate = edited.lower()

            print("Genre3 to update lowercase: ", genre3ToUpdate)

            # Discrepencies to the correction above are all handled here to ensure the game genre and
            # user profile genre preferences match
            if genre3ToUpdate == "2d":                  genre3ToUpdate = "twod"
            elif genre3ToUpdate == "class-based":       genre3ToUpdate = "class_based"
            elif genre3ToUpdate == "co-op":             genre3ToUpdate = "coop"
            elif genre3ToUpdate == "post-apocalyptic":  genre3ToUpdate = "post_apocalyptic"
            elif genre3ToUpdate == "sci-fi":            genre3ToUpdate = "scifi"

            print("Genre1 to update after validation: ", genre1ToUpdate)
            print("Genre2 to update after validation: ", genre2ToUpdate)
            print("Genre3 to update after validation: ", genre3ToUpdate)

            #Dynamically retrieves the user's preference value of the queried genre
            retrieve1 = getattr(user, genre1ToUpdate)
            print("Profile value: ", genre1ToUpdate, " = ", retrieve1)

            retrieve2 = getattr(user, genre2ToUpdate)
            print("Profile value: ", genre2ToUpdate, " = ", retrieve2)

            retrieve3 = getattr(user, genre3ToUpdate)
            print("Profile value: ", genre3ToUpdate, " = ", retrieve3)

            #Sets this queried genre to +1 of what it already was to learn they've shown interest in this genre
            setattr(user, genre1ToUpdate, retrieve1 + 1)
            setattr(user, genre2ToUpdate, retrieve2 + 1)
            setattr(user, genre3ToUpdate, retrieve3 + 1)

            #Save this change in the database
            user.save()
            print("User's ", genre1ToUpdate, " after incrementing = ", getattr(user, genre1ToUpdate))
            print("User's ", genre2ToUpdate, " after incrementing = ", getattr(user, genre2ToUpdate))
            print("User's ", genre3ToUpdate, " after incrementing = ", getattr(user, genre3ToUpdate))

    #TODO FOR MULTI GENRE SEARCH - return Game.objects.filter(genres__name=str('Action')).filter(genres__name=str('Side Scroller'))


class GamesPageByGenre(generic.ListView):
    template_name = 'games/genresearchresults.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        #Grabs the genre name and user's ID from the GenreSearch URL query, these are used to query all games with
        #the selected genre, and to then grab the profile of the currently logged in user to increment their preferences
        genre_name = self.request.GET.get("genre")
        user_id = self.request.GET.get("userid")

        #If the user is logged in then their preferences can be updated
        if user_id != "None":
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
            if genreToUpdate == "2d":                   genreToUpdate = "twod"
            elif genreToUpdate == "class-based":        genreToUpdate = "class_based"
            elif genreToUpdate == "co-op":              genreToUpdate = "coop"
            elif genreToUpdate == "post-apocalyptic":   genreToUpdate = "post_apocalyptic"
            elif genreToUpdate == "sci-fi":             genreToUpdate = "scifi"

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

    def get_context_data(self, **kwargs):
        context = super(GamesPageByGenre, self).get_context_data(**kwargs)

        genre_name = self.request.GET.get("genre")

        context['searched_genre'] = Genre.objects.filter(name=str(genre_name))
        return context

    #TODO FOR MULTI GENRE SEARCH - return Game.objects.filter(genres__name=str('Action')).filter(genres__name=str('Side Scroller'))


class Recommended(generic.ListView):
    template_name = 'games/recommended.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        user_id = self.request.GET.get("userid")

        if user_id != "None":
            user = Profile.objects.get(user_id=user_id)

            listOfGenres = ['twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                            'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'first_person',
                            'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                            'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                            'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                            'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie']

            #Create a list of preference values
            listOfPreferences = []
            for genre in listOfGenres:
                listOfPreferences.append(getattr(user, genre))

            #Create a list of corresponding genres and preference values joined together as a tuple
            userPreferences = list(zip(listOfGenres, listOfPreferences))

            #Sort the list of tuples by the preference value in descending order
            userPreferences.sort(key=itemgetter(1), reverse=True)

            listOfValidatedGenres = []

            #For the user's top 3 genres, ensure the case and spacing is correctly formatted
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

            #Return all games that match the top 3 genres, with no duplicates
            return Game.objects.filter(genres__name__in=[listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2]]).distinct().order_by('?')

            #TODO Order by ? is bad practice apparently, use this https://stackoverflow.com/questions/1731346/how-to-get-two-random-records-with-django#6405601
            #https://stackoverflow.com/a/12073921/6079009

    def get_context_data(self, **kwargs):
        context = super(Recommended, self).get_context_data(**kwargs)

        user_id = self.request.GET.get("userid")

        listOfValidatedGenres = []

        if user_id != "None":
            user = Profile.objects.get(user_id=user_id)

            listOfGenres = ['twod', 'action', 'adventure', 'arcade', 'building', 'cartoon', 'city_builder', 'class_based', 'coop', 'comedy',
                            'competitive', 'crafting', 'destruction', 'difficult', 'driving', 'dystopian', 'fantasy', 'first_person',
                            'fps', 'free_to_play', 'futuristic', 'historical', 'horror', 'indie', 'magic', 'medieval', 'military', 'moba',
                            'multiplayer', 'open_world', 'post_apocalyptic', 'procedural_generation', 'puzzle', 'racing', 'rpg', 'rts',
                            'sandbox', 'scifi', 'shooter', 'side_scroller', 'singleplayer', 'soccer', 'space', 'sports', 'stealth', 'strategy',
                            'survival', 'third_person', 'tower_defence', 'vr', 'war', 'zombie']

            listOfPreferences = []
            for genre in listOfGenres:
                listOfPreferences.append(getattr(user, genre))

            userPreferences = list(zip(listOfGenres, listOfPreferences))
            userPreferences.sort(key=itemgetter(1), reverse=True)

            serendipityGenreIndex = random.randint(26, 51)
            print("Serendipitous Genre Index = ", serendipityGenreIndex)

            # For their top 3 genres, ensure the case and spacing is correctly formatted
            for genre in range(4):
                currentGenre = ""

                if genre == 0 or genre == 1 or genre == 2:
                    currentGenre = userPreferences[genre][0]
                elif genre == 3:
                    currentGenre = userPreferences[serendipityGenreIndex][0]

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
                    currentGenre = currentGenre.upper()

                else:
                    capitalised = currentGenre[0:].capitalize()
                    currentGenre = capitalised

                # Add the corrected genre name to the list at the end of each loop
                listOfValidatedGenres.append(currentGenre)

        print("3 top genres = ", listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2])
        print("Serendipitous genre = ", listOfValidatedGenres[3])
        context['recommended_genres'] = Genre.objects.all().filter(name__in=[listOfValidatedGenres[0], listOfValidatedGenres[1], listOfValidatedGenres[2]])
        context['serendipitous_genre'] = Genre.objects.all().filter(name__in=[listOfValidatedGenres[3]])
        return context


# Displays all information about a single game on a detail page
class DetailPage(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        ProfileForm(request.POST)

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
