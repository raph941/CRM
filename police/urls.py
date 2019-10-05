from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path

from police import views

urlpatterns = [

    url(r"^NewPolice/$", views.NewPolice, name="new_police"),
    url(r"^MyProfile/(?P<pk>\d+)/$", views.MyProfile, name="my_profile"),
    url(r"^NewAdminPolice/$", views.NewAdminPolice, name="new_admin_police"),
    url(r"^ExistingPolice/$", views.ExistingPolice, name="existing_police"),
    url(r"^ExistingPolice/AdminList/$", views.AdminListView.as_view(), name="admin_list"),
    url(r"^ExistingPolice/PoliceList/$", views.PoliceListView.as_view(), name="police_list"),
    url(r"^ExistingPolice/PoliceList/(?P<pk>\d+)/$", views.ProfileView, name="police_profile_view"),
    url(r"^ExistingPolice/AdminList/(?P<pk>\d+)/$", views.ProfileView, name="admin_profile_view"),    
    
]
