from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm,ProfileForm
from .models import Profile,Location,NeighbourHood
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    

    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user      

    return render(request,"profile.html")
@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = EditProfileForm(instance=profile)
    if request.method == "POST":
            form = EditProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx) 
       
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})


