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
    fields = ('first_name','last_name', 'email', 'phone')
    list_display = ('first_name','last_name', 'email', 'phone', 'related_training_name',
                    'related_training_date', 'related_training_start_time')
    list_filter = ('first_name','last_name')
    list_display_links = None

    def related_training_name(self, obj):
        return obj.training.name
    related_training_name.short_description = 'Training name'

    def related_training_date(self, obj):
        return obj.training.training_date
    related_training_date.short_description = 'Training date'

    def related_training_start_time(self, obj):
        return obj.training.start_time
    related_training_start_time.short_description = 'Training start time'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Participant, ParticipantAdmin)


