from django.apps import apps
from django.shortcuts import render
from .models import About

Video = apps.get_model('video', 'Video')
Blog = apps.get_model('blog', 'Blog')
Album = apps.get_model('gallery', 'Album')
Picture = apps.get_model('gallery', 'Picture')


def index(request):
    about = About.objects.get(pk=1)
    albums = Album.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:6]
    pictures = Picture.objects.all().order_by('-id')[:10]
    videos = Video.objects.all().order_by('-id')[:3]
    context = {'about': about, 'albums': albums, 'blogs': blogs, 'pictures': pictures, 'videos': videos}
    return render(request, 'home/index.html', context)
