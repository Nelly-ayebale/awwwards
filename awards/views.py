from django.shortcuts import render,redirect
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from .forms import ProfileForm,ProjectForm,RatingForm,UserForm
from django.contrib.auth.decorators import login_required

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
