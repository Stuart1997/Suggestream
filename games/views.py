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


# Displays all results as a listview on the index page
def home(request):
    return render(request, 'games/index.html')


#TODO make this look at user's top X preferences
def recommended(request):
    return render(request, 'games/recommended.html')


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
    template_name = 'games/allgames.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        #Return games whose genres include the genre id x
        #return Game.objects.filter(genres__id=10)  /   return Game.objects.all().prefetch_related('genres')

        #Grabs the genre name and user's ID from the GenreSearch URL query, these are used to query all games with
        #the selected genre, and to then grab the profile of the currently logged in user to increment their preferences
        genre_id = self.request.GET.get("genre")
        user_id = self.request.GET.get("userid")
        user = Profile.objects.get(user_id=user_id)
        print("-----------------------------------")
        print("User = ", user)
        print("Genre = ", genre_id)
        print("User ID = ", user_id)
        print()

        #Replaces spaces with underscores as genres like "Class based" are "class_based" in preferences
        if " " in genre_id:
            edited = genre_id.replace(" ", "_")
            genreToUpdate = edited.lower()
        else:
            edited = genre_id
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

        #Once the preferences have been updated, retrieve all games that match the genre they selected
        return Game.objects.filter(genres__name=str(genre_id))


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
