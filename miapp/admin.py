from django.contrib import admin
from .models import Employee, Region

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class RegionAdmin(admin.ModelAdmin):
    readonly_fields = ('actualizado')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Region, RegionAdmin)