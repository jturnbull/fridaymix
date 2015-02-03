from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
import os

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^client_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "client_media")}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
         
    )

urlpatterns += patterns('',
    url(r'^tracks/$', 'mixes.views.tracks', name='tracks'),
    url(r'^(?P<slug>[\w-]+)/$', 'mixes.views.mix', name='mix'),
    url(r'^$', 'mixes.views.home', name='home'),
)