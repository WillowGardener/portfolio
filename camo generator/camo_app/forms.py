from django import forms
from .models import Camoimage

class ImageForm(forms.ModelForm):
    class Meta:
        model = Camoimage
        fields = ['old_image']