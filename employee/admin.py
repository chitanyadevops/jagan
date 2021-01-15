from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, Department
from .resources import EmployeeResource
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    #list_display = ('firstname','lastname','departmentid','designation','salary','phone_number')
    pass

admin.site.register(Department)