from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'games'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='register'),
]