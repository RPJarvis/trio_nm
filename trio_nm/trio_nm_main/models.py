from django.db import models
from django.core.urlresolvers import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, max_length=140)
    body = models.TextField()
    optional_image = models.ImageField(verbose_name="Optional Image", blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('newsitem.views.post', args=[self.slug])


class CalendarEvent(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField()
    location = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return u'%s' % self.title


class OfficerListing(models.Model):
    trio_title = models.CharField(max_length=40)
    name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=80)
    job_details = models.CharField(max_length=160)
    phone = models.CharField(max_length=14)
    optional_phone = models.CharField(max_length=14, blank=True)
    optional_fax = models.CharField(max_length=14, blank=True)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s' % self.name