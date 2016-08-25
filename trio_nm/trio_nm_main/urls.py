from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^our_mission', views.our_mission, name='our_mission'),
    url(r'^programs', views.programs, name='programs'),
    url(r'^events', views.events, name='events'),
    url(r'^news', views.news, name='news'),
    url(r'^scholarships', views.scholarships, name='scholarships'),
    url(r'^alumni', views.alumni, name='alumni'),
    url(r'^officers', views.officers, name='officers'),
    url(r'^$', views.index, name='index'), #this should be last

]