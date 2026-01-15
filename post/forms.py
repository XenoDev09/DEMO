from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post #models to be used
        fields=[
            'title',
            'description',
        ] #fields to be used