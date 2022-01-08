from django import forms
from django.db.models import fields
from watch.models import *
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact')
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','location','contact')     
class CreateCommunityForm(forms.ModelForm):
    class Meta:
        model=NeighbourHood
        fields =  ['community_image','community_description','name','location'] 
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields =  ['name','email','description','location','neighborhood']   

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','image','content','location','neighborhood']       

