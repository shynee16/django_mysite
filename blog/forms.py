from django import forms
from .models import Blog


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'seo_url', 'destination', 'picture_url', 'short_description', 'content']
