from django.apps import apps
from django.shortcuts import render, redirect
from .models import Blog
from .forms import SubmitForm

About = apps.get_model('home', 'About')

def index(request):
    about = About.objects.get(pk=1)
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'about': about, 'blogs': blogs})


def detail(request, seo_url):
    try:
        blog = Blog.objects.get(seo_url=seo_url)
        return render(request, 'blog/detail.html', {'blog': blog})
    except Blog.DoesNotExist:
        return render(request, 'blog/detail_not_found.html')

def submit(request):
    form = SubmitForm(request.POST)
    if form.is_valid():
        blog = form.save()
        return redirect('blog:index')
    return render(request, 'blog/addblog_form.html', {'form':form})
