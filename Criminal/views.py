from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from django.urls import reverse
from django.core.paginator import Paginator

from Criminal.forms import NewCriminalForm
from Criminal.forms import NewCrimeForm
from .models import Criminal
from .models import Crime
from police.models import PoliceProfile, User


@login_required
def WantedList(request):
    return render(request, 'wanted_list.html')


@login_required
def CrimeRecord(request):
    return render(request, 'crime_record.html')


@login_required
def Criminals(request):
    return render(request, 'criminals.html')


@login_required
def AddCriminals(request):
    form = NewCriminalForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form_data = form.save()
            form_data.save()
            pk = form_data.pk

            return redirect('criminal_profile1', pk)
        else:
            form = NewCriminalForm

    return render(request, 'add_criminals.html', {'form': form})


def CriminalProfile1(request, pk):
    criminal = Criminal.objects.get(pk=pk)

    return render(request, 'criminalprofile1.html', {'criminal': criminal})


def success(request):
    return HttpResponse('successful upload')


class CriminalListView(ListView):
    template_name = 'criminal_list.html'
    queryset = Criminal.objects.all()
    context_object_name = 'criminals'
    paginate_by = 10


class WantedListView(ListView):
    model = Criminal
    template_name = 'wanted_list.html'
    queryset = Criminal.objects.all().filter(wanted_status='WANTED')
    context_object_name = 'criminals'
    paginate_by = 10



@login_required
def NewCrimeView(request):
    form = NewCrimeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form =  NewCrimeForm(request.POST)
            form.save()
            return redirect('crime_list')
        else:
            form = NewCrimeForm(request.POST)
    return render(request, 'new_crime.html', {'form': form})

class CrimeListView(ListView):
    model = Crime
    template_name = 'crime_list.html'
    context_object_name = 'crimes'
    paginate_by = 10
    queryset = Crime.objects.all()
    # import pdb; pdb.set_trace()
    # me=345


class CrimeDetailView(DetailView):
    model = Crime
    template_name = 'crime_detail.html'
    

@login_required
def SearchBiometrics(request):
    return render(request, 'search_biometrics.html')


@login_required
def NewBiometrics(request):
    return render(request, 'new_biometrics.html')
