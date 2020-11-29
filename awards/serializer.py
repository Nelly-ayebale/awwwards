from rest_framework import serializers
from .models import Profile,Project
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','image','description','project_link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        projects = ProjectSerializer()
        model = Profile
        fields = ('name','profile_photo','bio','contact','projects')


