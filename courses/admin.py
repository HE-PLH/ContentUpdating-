from django.contrib import admin


from .models import Course, Unit
# Register your models here.
admin.site.register(Course)
admin.site.register(Unit)