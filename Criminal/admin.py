from django.contrib import admin
from .models import Criminal
from .models import CriminalImage
from .models import Crime

# Register your models here.
admin.site.register(Criminal)
admin.site.register(CriminalImage)
admin.site.register(Crime)