from django.contrib import admin
from .models import Training
from .models import Instructor
from .models import TrnDesc

admin.site.register(Instructor)

class TrnDescAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

admin.site.register(TrnDesc, TrnDescAdmin)

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_date', 'name', 'instructor', 'start_time', 'end_time')
    
admin.site.register(Training, TrainingAdmin)


