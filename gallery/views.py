from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Picture
from .forms import AddAlbumForm, UploadPhotoForm


def index(request):
    pictures = Picture.objects.all().order_by('-date_uploaded')[:15]
    return render(request, 'gallery/index.html', {'pictures': pictures})


def albums(request):
    albums = Album.objects.all().order_by('-date_created')
    return render(request, 'gallery/albums.html', {'albums': albums})


def album_details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    pictures = Picture.objects.all().filter(album=album).order_by('-date_uploaded')
    return render(request, 'gallery/album_pictures.html', {'album': album, 'pictures': pictures})


def upload_photo(request, album_id=False):
    form = UploadPhotoForm(request.POST, request.FILES)
    albums = Album.objects.all().order_by('-date_created')
    if (album_id):
        selected_album = get_object_or_404(Album, pk=album_id)
    else:
        selected_album = albums[0]
    pictures = Picture.objects.all().filter(album=selected_album).order_by('-date_uploaded')
    if form.is_valid():
         for uploaded_picture in request.FILES.getlist('picture'):
            picture = Picture.objects.create(album=selected_album)
            picture.picture_url = uploaded_picture
            picture.save()
    return render(request, 'gallery/upload_photo_form.html', {'albums': albums, 'selected_album': selected_album, 'pictures': pictures})


def add_album(request):
    form = AddAlbumForm(request.POST, request.FILES)
    if form.is_valid():
        album = form.save(commit=False)
        album.cover_url = request.FILES['cover']
        album.save()
        return redirect('gallery:album_details', album.pk)
    return render(request, 'gallery/album_form.html')
