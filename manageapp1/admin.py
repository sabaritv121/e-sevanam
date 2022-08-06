from django.contrib import admin

# Register your models here.
from .import models

admin.site.register(models.Login)
admin.site.register(models.Government)
admin.site.register(models.Department)
admin.site.register(models.Complaints)
admin.site.register(models.User)
admin.site.register(models.AppointmentSchedule)
admin.site.register(models.Appointment)
admin.site.register(models.Uploads)