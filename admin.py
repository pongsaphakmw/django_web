from django.contrib import admin
from .models import Examscore ,AllStudent


admin.site.register(Examscore)

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student_id','level','student_name','student_tel']
	list_filter = ['level']
	list_editable = ['student_tel']


admin.site.register(AllStudent, StudentAdmin)
