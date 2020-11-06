from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from Criminal import views


urlpatterns = [

    url(r"^AddCriminals/$", views.AddCriminals, name="add_criminals"),
    url(r"^CriminalProfile/(?P<pk>\d+)/$", views.CriminalProfile1, name="criminal_profile1"),
    url(r"^success/$", views.success, name="success"),
    url(r"^ViewCriminal/$", views.CriminalListView.as_view(), name="criminal_list"),
    url(r"^ViewCriminal/(?P<pk>\d+)/DeleteCriminal/$", views.CriminalDeleteView.as_view(), name="criminal_delete"),

    url(r"^WantedList/$", views.WantedListView.as_view(), name="wanted_list"),
    url(r"^CrimeList/$", views.CrimeListView.as_view(), name="crime_list"),
    url(r"^NewCrime/$", views.NewCrimeView, name="new_crime"),
    url(r"^CrimeList/CrimeDetail/(?P<pk>\d+)/$", views.CrimeDetailView.as_view(), name="crime_detail"),
    url(r"^SearchBiometrics/$", views.SearchBiometrics, name="search_biometrics"),
    url(r"^NewBiometrics/$", views.NewBiometrics, name="new_biometrics"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)