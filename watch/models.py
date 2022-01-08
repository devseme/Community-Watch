from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    # save location
    def save_location(self):
        self.save()

    def _str_(self):
        return self.name
# NeighbourHood Model
class NeighbourHood(models.Model):
    community_image = CloudinaryField('community_image',null=True)
    community_description = models.TextField(max_length=250,null=True)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_neigbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    # find neighbourhood by id
    @classmethod
    def find_neigbourhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def _str_(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)   
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Location, null=True,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,related_name ='members',on_delete=models.CASCADE,null=True)


    def str(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def _str_(self):
        return self.user.username


class Business(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    description = models.TextField(blank=True)
    neighborhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    # def update_business(self):
    #     self.update()    

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    def _str_(self):
        return self.name 
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name        
#Post model
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    image=CloudinaryField('image',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    def _str_(self):
        return self.title           

