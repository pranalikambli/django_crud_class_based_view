from django import forms
from .models import Blogs


class BlogForm(forms.ModelForm):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    excerpt = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Blogs
        fields = ['title', 'slug', 'excerpt', 'content', 'status', 'author']