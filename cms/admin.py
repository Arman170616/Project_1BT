from django.contrib import admin
from .models import HomePageContent

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fr')