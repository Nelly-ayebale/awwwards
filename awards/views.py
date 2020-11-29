from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from .forms import ProfileForm,ProjectForm,RatingForm,UserForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    users = User.objects.exclude(id=request.user.id)
    projects = Project.all_projects()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()

            return redirect('home')
    else:
        form = ProjectForm()
    return render(request,'awards/home.html',{"users":users,"projects":projects,"form":form})

@login_required(login_url='accounts/login/')
def profile(request, username):
    projects = request.user.profile.projects.all()

    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'awards/profile.html',{"user_form":user_form,"profile_form":profile_form,"projects":projects})

@login_required(login_url='accounts/login/')
def user(request,username):
    user_form = get_object_or_404(User, username=username)

    if request.user == user_form:
        return redirect('profile',username=request.user.username)
    projects = user_form.profile.projects.all()

    return render(request,'awards/user.html',{"user_form":user_form,"projects":projects})

@login_required(login_url='accounts/login/')
def search_by_title(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awards/search.html',{"message":message})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
