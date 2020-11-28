from django import forms
from django.contrib.auth.models import User
from .models import Profile,Project,Rating

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_photo','bio','contact']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','image','description','project_link']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design','usability','content']