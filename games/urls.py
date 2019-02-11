from django.urls import path
from . import views
from django.urls import path, include
from games import views as game_views

app_name = 'games'

urlpatterns = [
    path('', views.home, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='register'),
    path('<pk>/detail', views.DetailPage.as_view(), name='detail'),
    path('favourites/', game_views.SelectFavouriteGenres.as_view(), name='favourites'),
    path('favourites/submitted/', game_views.SubmitFavourites.as_view(), name='submitted'),
]
