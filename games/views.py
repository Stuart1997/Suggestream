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
from .models import Game, Genre
from .forms import UserRegisterForm


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


# Displays all information about a single game on a detail page
class DetailPage(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'games/register.html', {'form': form})    #Refer to the form object within the next page


#Prevents this view from being accessed if the user isn't logged in
@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'games/profile.html', args)


#If the url doesn't have anything after the slash, redirect them to the login page
def login_redirect(request):
    return redirect('games:login')


def login_prompt(request):
    return redirect('games:login')
