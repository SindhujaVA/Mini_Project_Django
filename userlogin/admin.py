from django.contrib import admin
from .models import User

# Register your models here.

class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    list_filter = ('username',)

admin.site.register(User,MyCustomAdmin)
