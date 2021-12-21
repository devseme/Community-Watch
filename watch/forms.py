from django import forms
from django.db.models import fields
from watch.models import Profile



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact')
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact')          