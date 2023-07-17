from django.contrib import admin
from .models import Academia


@admin.register(Academia)
class AcademiaAdmin(admin.ModelAdmin):
    pass
