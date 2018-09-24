from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee
import csv

@admin.register(Employee)
class ViewAdmin(ImportExportModelAdmin):
    pass