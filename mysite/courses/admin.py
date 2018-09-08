from django.contrib import admin

# Register your models here.
from .models import Courses

#admin.site.register(Courses)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('friendly_course', 'friendly_distance', 'index_number')
    list_filter = ('friendly_course',)

admin.site.register(Courses , CoursesAdmin)
