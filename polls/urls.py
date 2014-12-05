from django.conf.urls import url, patterns
from polls import views
#from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

 #   url(r'^polls/', include('polls.urls')),
 #   url(r'^admin/', include(admin.site.urls)),
    
)

