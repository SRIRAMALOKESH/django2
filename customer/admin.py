from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserAccount, UserAccountAdmin)
