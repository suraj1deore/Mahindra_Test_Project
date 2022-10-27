from django.contrib import admin
from .models import ImportData
from import_export.admin import ImportExportModelAdmin

@admin.register(ImportData)
class Personadmin(ImportExportModelAdmin):
    data = ("category","X","Y")