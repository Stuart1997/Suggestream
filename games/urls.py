from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'games'

urlpatterns = [
    path('', views.home, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='register'),
    path('<pk>/detail', views.DetailPage.as_view(), name='detail'),
]
