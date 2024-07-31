from django.shortcuts import render
from .models import Video, Song

def index(request):
    return render(request, 'personal_website/index.html')

def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'personal_website/videos_list.html', {'videos': videos})

def songs_list(request):
    songs = Song.objects.all()
    return render(request, 'personal_website/songs_list.html', {'songs': songs})
