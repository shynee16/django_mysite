from django import forms
from .models import Album, Picture

class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'caption']

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['album']
