from django.contrib import admin
from .models import formdeets

# Register your models here.
# class formdeetsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'qualified', 'ans1', 'ans2', 'ans3', 'ans4')
  
#     def active(self, obj):
#         return obj.is_active == 1
  
#     active.boolean = True

admin.site.register(formdeets)