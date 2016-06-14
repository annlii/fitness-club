from django.contrib import admin
from .models import Training
from .models import Instructor

# Register your models here.
admin.site.register(Training)
admin.site.register(Instructor)
