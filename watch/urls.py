from django.urls import path
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('create_community',views.create_community,name = 'create_community'),
    path('community/',views.community,name = 'community'),
    path('singlecommunity/<str:name>',views.singlecommunity,name = 'singlecommunity'),
    path('join_community/<int:id>', views.join_community, name='join_community'),
    path('leave_community/<int:id>', views.leave_community, name='leave_community'),
    path("create_business", views.create_business, name="create_business"),
    path("businesses/", views.businesses, name="businesses"),
    path('post/create_post', views.create_post, name='create_post'),
    path('posts/', views.posts, name = 'post'),
    
  
]