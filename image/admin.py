from django.contrib import admin
from .models import Photo, Person

# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'caption', 'photo', 'desc']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name',
                    'last_name', 'gender', 'mobile', 'address']
