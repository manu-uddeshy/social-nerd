from groups.models import GroupMember
from django.contrib import admin
from . import models
# Register your models here.

class GroupMemerInline(admin.TabularInline):
    model = models.GroupMember 

admin.site.register(models.Group)
