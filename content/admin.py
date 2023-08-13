from django.contrib import admin

# Register your models here.
from .models import Topic, Content
# Register your models here.
admin.site.register(Topic)
admin.site.register(Content)