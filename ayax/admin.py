from django.contrib import admin

from .models import Subdivision, Realtor


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'registered')
    list_display_links = ('name', 'registered')
    search_fields = ('name', 'registered')


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'subdivision', 'registered')
    list_display_links = ('name', 'surname', 'subdivision', 'registered')
    search_fields = ('surname', 'name', 'registered')


admin.site.register(Subdivision, SubdivisionAdmin)
admin.site.register(Realtor, RealtorAdmin)
