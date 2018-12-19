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
from .models import Game
from .forms import UserForm
from .forms import UserRegisterForm


# Displays all results as a listview on the index page
class IndexPage(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.all()


# Displays all information about a single game on a detail page
class DetailPage(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'games/registration_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Submit form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # Creates object from form without saving to db

            # Cleaned/normalised data - formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user.set_password(password)  # Handles hashed password instead of plaintext
            user.save()  # Saves to db

            # Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)  # Checks if they exist in db

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('games:index')

        return render(request, self.template_name, {'form': form})


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
    return redirect('games:index')


def login_prompt(request):
    return redirect('games:login')
