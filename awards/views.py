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


