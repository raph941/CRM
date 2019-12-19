from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django import forms
from django.urls import reverse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
import mimetypes
import os
from django.conf import settings

from Criminal.forms import NewCriminalForm
from Criminal.forms import NewCrimeForm, FingerprinttemplateForm
from .models import Criminal, FingerPrint
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
    # fingerprinttemplates = FingerPrint.objects.get(criminal_id=pk)

    # fl_path = os.path.join(settings.MEDIA_ROOT, fingerprinttemplates)
    # filename = 'right_thumb.ftp'

    # fl = open(fl_path, 'r')
    # mime_type, _ = mimetypes.guess_type(fl_path)
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # return response

    context = {
        'criminal': criminal,
        # 'fingerprinttemplates': fingerprinttemplates,
    }
    
    return render(request, 'criminalprofile1.html', context)


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


class CriminalDeleteView(DeleteView):
    model = Criminal
    success_url = reverse_lazy('criminal_list')
    template_name = 'criminal_delete.html'

    

@login_required
def SearchBiometrics(request):
    return render(request, 'search_biometrics.html')


@login_required
def NewBiometrics(request):
    form = FingerprinttemplateForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form_data = form.save()
            form_data.save()
            messages.success(request, "Fingerprint Template was Successfully Uploaded!", extra_tags='alert')
            return redirect('new_biometrics')
        else:
            form = FingerprinttemplateForm
            messages.error(request, 'Fingerprint Upload Was Unsuccessful!')
    return render(request, 'new_biometrics.html', {'form': form})
