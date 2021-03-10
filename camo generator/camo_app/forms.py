from django import forms
from .models import Camoimage

class ImageForm(forms.ModelForm):
    class Meta:
        model = Camoimage
        fields = ['brush_size','old_image']