from django.contrib import admin

# Register your models here.
from .models import Categories,Countries,Products

admin.site.register(Categories)
admin.site.register(Countries)
admin.site.register(Products)
