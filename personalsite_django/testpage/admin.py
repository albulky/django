from django.contrib import admin

# Register your models here.
from .models import FooTest


class FooTestAdmin(admin.ModelAdmin):
    list_display = ('foo', 'dt_create', 'dt_edit', 'user', 'ord')
    ordering = ('ord','dt_create','foo')
    search_fields = ('dt_create', 'foo')
 
admin.site.register(FooTest, FooTestAdmin)