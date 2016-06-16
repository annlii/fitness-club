from django.contrib import admin
from .models import Training
from .models import Instructor
from .models import TrnDesc

admin.site.register(Training)
admin.site.register(Instructor)
admin.site.register(TrnDesc)


