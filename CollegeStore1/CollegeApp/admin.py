from django.contrib import admin
from .models import Department,StudentForm,Purposes,Courses

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentForm)
admin.site.register(Purposes)
admin.site.register(Courses)

