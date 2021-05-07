from django.contrib import admin
from .models import Fcuser

class fcuserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
admin.site.register(Fcuser, fcuserAdmin)
