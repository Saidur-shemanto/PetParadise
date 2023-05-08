from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.rescueApply)
class rescueApplicants(admin.ModelAdmin):
    list_display = ['applicant_username', 'experience', 'applicant_membership']
    list_editable = []

    def applicant_username(self, obj):
        return obj.applicant.username
    applicant_username.short_description = 'Applicant username'

    def applicant_membership(self, obj):
        return obj.applicant.membership_stat
    applicant_membership.short_description = 'Applicant membership'
