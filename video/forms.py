from django import forms
from .models import Video


class UploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'destination', 'video_url', 'embed_url', 'thumb_url']
