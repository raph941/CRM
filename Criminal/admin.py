from django.contrib import admin
from .models import Criminal
from .models import Crime

# Register your models here.
admin.site.register(Criminal)
admin.site.register(Crime)