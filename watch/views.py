from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm,ProfileForm,CreateCommunityForm,BusinessForm,PostForm
from .models import Profile,Location,NeighbourHood,Business,Post
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
    profile = Profile.objects.filter(user_id=current_user.id).first()    

    return render(request,"profile.html",{'profile':profile})
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

@login_required(login_url='/accounts/login/')
def create_community(request):
    current_user = request.user
    if request.method == 'POST':
        community_form = CreateCommunityForm(request.POST,request.FILES)
        if community_form.is_valid():

            community = community_form.save(commit=False)
            community.user = current_user
            community.save()

        return HttpResponseRedirect('/profile')
    else:
        community_form = CreateCommunityForm()

    context = {'community_form':community_form}
    return render(request,'community/create_community.html',context)

@login_required(login_url='/accounts/login/')
def community(request):
    current_user = request.user
    community = NeighbourHood.objects.all().order_by('-id')

    context = {'community':community}
    return render (request,'community/community.html',context)

@login_required(login_url='/accounts/login/')
def singlecommunity(request,name): 
    community = NeighbourHood.objects.get(name=name) 
   

    return render(request,'community/single_community.html',{'community':community})  

@login_required(login_url='/accounts/login/')
def join_community(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('community')

@login_required(login_url='/accounts/login/')
def leave_community(request, id):
    community = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('community')

@login_required(login_url='/accounts/login/')
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.community= community
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
            form=BusinessForm()
    return render (request,'business/create_business.html', {'form': form, 'profile': profile})

@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    businesses = Business.objects.all().order_by('-id')
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        
        businesses = Business.objects.all().order_by('-id')
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighbourhood": neighbourhood, "businesses": businesses})
    else:
        neighbourhood = profile.neighbourhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "business/business.html", {"businesses": businesses})

login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.community = community
            post.user=current_user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.filter(user_id=current_user.id)
        
        locations = Location.objects.all()
        neighborhood = NeighbourHood.objects.all()
        
        businesses = Business.objects.filter(user_id=current_user.id)
        
        return render(request, "profile.html", {"danger": "Update Profile ", "locations": locations, "neighborhood": neighborhood,  "businesses": businesses,"posts": posts})
    else:
        neighborhood = profile.neighbourhood
        posts = Post.objects.filter(user_id=current_user.id)
        return render(request, "posts/posts.html", {"posts": posts})          









