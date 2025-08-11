from django.contrib import admin
from .models import Database_model

# Register your models here.


class DBadmin(admin.ModelAdmin):
    list_display=('firstname','lastname','joined_date')


admin.site.register(Database_model,DBadmin)