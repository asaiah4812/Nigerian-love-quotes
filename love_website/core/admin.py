from django.contrib import admin
from .models import Category, Quote
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class QuoteAdmin(ImportExportModelAdmin):
    list_display = ['id', 'author', 'msg', 'category']

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Category)
