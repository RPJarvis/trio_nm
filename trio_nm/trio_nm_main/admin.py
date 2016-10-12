from django.contrib import admin
from . import models
# Register your models here.


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'optional_image', 'publish_date']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.NewsItem, NewsItemAdmin)


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'description', 'optional_link']


admin.site.register(models.CalendarEvent, CalendarEventAdmin)


class OfficerListingAdmin(admin.ModelAdmin):
    list_display = ['trio_title', 'name', 'job_title', 'job_details', 'phone', 'optional_phone',
                    'optional_fax', 'email']


admin.site.register(models.OfficerListing, OfficerListingAdmin)


class ScholarshipListingAdmin(admin.ModelAdmin):
    list_display = ['scholarship_name', 'application_deadline', 'application_link', 'contact']


admin.site.register(models.ScholarshipListing, ScholarshipListingAdmin)


class AchieverProfileAdmin(admin.ModelAdmin):
	list_display = ['headline', 'optional_posting_date', 'text_body', 'optional_image']

admin.site.register(models.AchieverProfile, AchieverProfileAdmin)


