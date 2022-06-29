from django.contrib import admin
from .models import Puppy


class PuppyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Puppy, PuppyAdmin)