"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls import url
from police import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from police.views import SearchResultView


urlpatterns = [
    url(r'^$', views.home, name='home'),     

    path('police/', include('police.urls')),
    path('Criminal/', include('Criminal.urls')),

    url(r"^SearchResult/$", SearchResultView.as_view(), name="search_results"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login.html'}, name='logout'),
    url(r"^Dashboard/$", views.Dashboard, name="dashboard"),
    url(r'^admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)