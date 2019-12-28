# import requests
import json
from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from Criminal.models import Criminal
from Criminal.models import Crime
from django.db.models import Q, Count
from itertools import chain
from django.core.paginator import Paginator

from police.forms import AdminPoliceCreationForm, PoliceCreationForm, UserUpdateForm, UserProfileUpdateForm, BackgroundCreationForm
from Criminal.forms import SelectStateForAnalysisForm

from .models import PoliceProfile, User
from .LGA_COUNT import *


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def About(request):
    return render(request, 'about.html')

class SearchResultView(ListView):
    template_name = 'search_results.html'
    context_object_name = 'searched_criminals'
    paginate_by = 3
    
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            or_lookup_criminal = (
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
                )
            or_lookup_crime = (
                Q(type__icontains=query) |
                Q(crime_status__icontains=query)
                )
            criminal_result = Criminal.objects.filter(or_lookup_criminal)
            crime_result = Crime.objects.filter(or_lookup_crime)

            queryset_chain = chain(
                criminal_result,
                crime_result
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk, 
                        reverse=True)
            return qs
        return Criminal.objects.none()       

        
@login_required
def Dashboard(request):
    form = SelectStateForAnalysisForm(request.GET)
    criminal_count = Criminal.objects.count
    crime_count = Crime.objects.count
    police_count = User.objects.count
    wanted_list_count = Criminal.objects.filter(wanted_status='WANTED').count
    
    dataset = Crime.objects.values('state_of_crime').annotate(number_of_crimes = Count('state_of_crime'))
    
    categories = list()
    number_of_crimes = list()

    for entry in dataset:
        categories.append(entry['state_of_crime'])
        number_of_crimes.append(entry['number_of_crimes'])


    context = {
        'criminal_count': criminal_count,
        'crime_count': crime_count,
        'police_count': police_count,
        'wanted_list_count': wanted_list_count,
        'categories': json.dumps(categories),
        'number_of_crimes': json.dumps(number_of_crimes),
        'form': form,
    }

    return render(request, 'dashboard.html', context)


@login_required
def States(request):
    dataset = Crime.objects.values('local_gov_area').annotate(number_of_crimes = Count('local_gov_area'))
    
    categories = list()
    number_of_crimes = list()

    for entry in dataset:
        categories.append(entry['local_gov_area'])
        number_of_crimes.append(entry['number_of_crimes'])


    context = {
        'categories': json.dumps(categories),
        'number_of_crimes': json.dumps(number_of_crimes),
    }
   
    return render(request, 'plateau.html', context, context2)


@login_required
def NewPolice(request):
    form = PoliceCreationForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_police = True
            user.save()
            police_id = form.cleaned_data.get('police_id')
            phone_number = form.cleaned_data.get('phone_number')
            nationality = form.cleaned_data.get('nationality')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            profile_pic = form.cleaned_data.get('profile_pic')

            PoliceProfile.objects.create(police_id=police_id, phone_number=phone_number,
                                         nationality=nationality,
                                         state=state, city=city, profile_pic=profile_pic, user=user)
            messages.success(request, "successfully Created")
            return redirect('home')
        else:
            messages.success(request, "user was not successfully Created")
            form = PoliceCreationForm()

    return render(request, 'new_police.html', {'form': form})


@login_required
def NewAdminPolice(request):
    form = AdminPoliceCreationForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_admin_police = True
            user.save()
            police_id = form.cleaned_data.get('police_id')
            phone_number = form.cleaned_data.get('phone_number')
            nationality = form.cleaned_data.get('nationality')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            profile_pic = form.cleaned_data.get('profile_pic')

            PoliceProfile.objects.create(police_id=police_id, phone_number=phone_number,
                                         nationality=nationality,
                                         state=state, city=city, profile_pic=profile_pic, user=user)
            messages.success(request, "successfully Created")
            return redirect('home')
        else:
            messages.success(request, "user was not successfully Created")
            form = AdminPoliceCreationForm()

    return render(request, 'new_admin_police.html', {'form': form})


@login_required
def NewBackgroundCheck(request):
    form = BackgroundCreationForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_background_check = True
            user.save()
            
            messages.success(request, "successfully Created")
            return redirect('home')
        else:
            messages.success(request, "user was not successfully Created")
            form = BackgroundCreationForm()

    return render(request, 'new_background_check.html', {'form': form})



@login_required
def ExistingPolice(request):
    return render(request, 'existing_police.html')


class AdminListView(ListView):
    template_name = 'admin_list.html'
    queryset = User.objects.all().filter(is_admin_police=True)
    context_object_name = 'administrative_users'
    paginate_by = 10


class PoliceListView(ListView):
    template_name = 'police_list.html'
    queryset = User.objects.all().filter(is_police=True)
    context_object_name = 'users'
    paginate_by = 10


@login_required
def ProfileView(request, pk):
    profile = User.objects.get(pk=pk)

    return render(request, "profile_view.html", {'profile': profile})

# this view is surposed to update user profile but it not working yet so take note and fix it laters
@login_required
def MyProfile(request, pk):   
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        upu_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.policeprofile)
        if uu_form.is_valid and upu_form.is_valid():
            uu_form.save()
            upu_form.save()
            return redirect('home')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        upu_form = UserProfileUpdateForm(instance=request.user.policeprofile)

    context = {
        'uu_form': uu_form,
        'upu_form': upu_form,
    }
    return render(request, "my_profile.html", context)



