from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=60,blank=True)
    profile_photo = CloudinaryField('image',blank=True)
    bio = models.TextField()
    contact = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.user
    
    def delete_profile(self):
        self.delete()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    
class Project(models.Model):
    profile = models.ForeignKey('Profile',on_delete=models.ForeignKey,related_name='projects')
    title = models.CharField(max_length=300)
    image = CloudinaryField('image',blank=True)
    description = models.TextField(blank=True)
    project_link = models.URLField(max_length=300)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()

    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_by_title(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles


class Rating(models.Model):
    rating = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'))
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rater',blank=True)
    project = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='rating',blank=True)
    design = models.IntegerField(choices=rating,blank=True,default=0)
    usability = models.IntegerField(choices=rating,blank=True,default=0)
    content = models.IntegerField(choices=rating,blank=True,default=0)
    score = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.rating
    
    def save_rating(self):
        self.save()
    
    @classmethod
    def get_rating_by_id(cls,id):
        ratings = Rating.objects.filter(profile_id=id).all()
        return ratings

    



# Create your models here.
