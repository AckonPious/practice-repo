from django.contrib import admin
from .models import Members

# Register your models here.
class Membersadmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

admin.site.register(Members, Membersadmin)
