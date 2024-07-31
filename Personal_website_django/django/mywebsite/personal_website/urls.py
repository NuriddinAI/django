from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.videos_list, name='videos_list'),
    path('songs/', views.songs_list, name='songs_list'),
]

