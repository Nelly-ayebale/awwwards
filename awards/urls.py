from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('profile/<username>/',views.profile,name='profile'),
    path('user/<username>/',views.user,name='user'),
    path('search/', views.search_by_profile, name='search'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/projects/',views.ProjectList.as_view()),
]
