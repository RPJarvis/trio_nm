from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^our_mission', views.our_mission, name='our_mission'),
    url(r'^programs', views.programs, name='programs'),
    url(r'^events', views.events, name='events'),
    url(r'^news', views.news, name='news'),
    url(r'^events', views.events, name='events'),
    url(r'^fair_share', views.fair_share, name='fair_share'),
    url(r'^scholarships', views.scholarships, name='scholarships'),
    url(r'^alumni', views.alumni, name='alumni'),
    url(r'^officers', views.officers, name='officers'),
    url(r'^achiever', views.achiever, name='achiever'),
    url(r'^committee', views.committee, name='committee'),
    url(r'^(?P<slug>[\w\-]+)/$', views.event_post, name='event_post'),
    url(r'^$', views.index, name='index'), #this should be last

]