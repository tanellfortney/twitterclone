
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Image
#         fields = ('title', 'image')
