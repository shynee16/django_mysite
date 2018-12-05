from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.albums, name='albums'),
    path('album/upload/<int:album_id>/', views.upload_photo, name='upload_photo'),
    path('album/add/', views.add_album, name='add_album'),
    path('album/<int:album_id>/', views.album_details, name='album_details'),
]
