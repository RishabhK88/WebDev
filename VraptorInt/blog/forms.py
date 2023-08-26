from django import forms

from .models import Post


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Email = forms.EmailField()
    Subject = forms.CharField(max_length=400)
    Message = forms.TextInput()

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = []


class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class'      : 'form-control mr-sm-2',
        'placeholder': '',
        'aria-label' : 'Search',
    }))
