from django.contrib import admin
from MyApp.models import User,Dept,Doctor,Patient,Work,Room,Deal_method,Medicine
admin.site.register(User)
class DeptAdmin(admin.ModelAdmin):
    list_display=['dept_name','dept_manager','dept_manager']
    fields = ('dept_name',)
    search_fields = ['dept_name']
admin.site.register(Dept,DeptAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Work)
admin.site.register(Room)
admin.site.register(Deal_method)
admin.site.register(Medicine)
