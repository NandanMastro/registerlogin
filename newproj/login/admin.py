from django.contrib import admin
from .models import account,User_info
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.register(User_info)
# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(account)
