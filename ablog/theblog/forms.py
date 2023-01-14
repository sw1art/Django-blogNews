from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input title'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input tag-link'}),
            'author': forms.Select(attrs={
                'class': 'form-control',}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Input a message post"}),
        }