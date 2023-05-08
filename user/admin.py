from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.userprofile)
class users(admin.ModelAdmin):
    list_display = ['username', 'membership_stat']
    list_editable = ['membership_stat']


