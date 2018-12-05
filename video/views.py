from django.apps import apps
from django.shortcuts import render, redirect
from .models import Video
from .forms import UploadForm

Blog = apps.get_model('blog', 'Blog')


def index(request):
    blogs = Blog.objects.all().order_by('-id')[:3]
    destinations = Video.objects.values('destination').distinct()
    videos = Video.objects.all()
    return render(request, 'video/index.html', {'blogs': blogs, 'videos': videos, 'destinations': destinations})


def place(request, destination_value):
    blogs = Blog.objects.all().order_by('-id')[:2]
    destinations = Video.objects.values('destination').distinct()
    videos = Video.objects.filter(destination=destination_value)
    return render(request, 'video/index.html', {'blogs': blogs, 'videos': videos, 'destinations': destinations})


def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        video = form.save(commit=False)
        video.thumb_url = request.FILES['thumb']
        video.save()
        return redirect('video:index')
    return render(request, 'video/video_form.html')
