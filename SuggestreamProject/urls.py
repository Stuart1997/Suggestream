from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from games import views as game_views


urlpatterns = [
    path('', game_views.login_redirect, name='login_redirect'),
    path('home/', include('games.urls', namespace='home')),
    path('games-alphabetical/', game_views.GamesPageAlphabetically.as_view(), name='all-alphabetical'),
    path('games-rating/', game_views.GamesPageByRating.as_view(), name='all-metacritic'),
    path('recommended/', game_views.Recommended.as_view(), name='recommended'),
    path('genre-search/', game_views.GenreSearch.as_view(), name='genre-search'),
    path('genre-results/', game_views.GamesPageByGenre.as_view(), name='genre-results'),
    path('title-search/', game_views.TitleSearch.as_view(), name='title-search'),
    path('register/', game_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='games/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='games/logout.html'), name='logout'),
    path('profile/', game_views.profile, name='profile'),
    path('favourites/', game_views.SelectFavouriteGenres.as_view(), name='favourites'),
    path('favourites/submitted/', game_views.SubmitFavourites.as_view(), name='submitted'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
