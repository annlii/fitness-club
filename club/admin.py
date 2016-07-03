from django.contrib import admin
from .models import Training
from .models import Instructor
from .models import TrnDesc
from .models import Participant

admin.site.register(Instructor)

class TrnDescAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

admin.site.register(TrnDesc, TrnDescAdmin)

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_date', 'name', 'instructor', 'start_time', 'end_time')
    
admin.site.register(Training, TrainingAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'phone', 'training')

admin.site.register(Participant, ParticipantAdmin)


