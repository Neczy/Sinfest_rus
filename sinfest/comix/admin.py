from django.contrib import admin
from .models import Comix

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')

admin.site.register(Comix)