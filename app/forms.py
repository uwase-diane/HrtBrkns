from django import forms
from .models import Profile,Project,Comments
from django.forms import ModelForm,Textarea,IntegerField


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','projects']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','projects']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['posted_by', 'commented_project','user']
