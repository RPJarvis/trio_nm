from django.contrib import admin
from . import models
# Register your models here.


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'optional_image', 'publish_date']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.NewsItem, NewsItemAdmin)


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'description']


admin.site.register(models.CalendarEvent, CalendarEventAdmin)


class OfficerListingAdmin(admin.ModelAdmin):
    list_display = ['trio_title', 'name', 'job_title', 'job_details', 'phone', 'optional_phone',
                    'optional_fax', 'email']


admin.site.register(models.OfficerListing, OfficerListingAdmin)