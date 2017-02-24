from django.contrib import admin
from .models import publicacion

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(publicacion)