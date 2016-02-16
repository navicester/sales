#from django.conf.urls import patterns, include, url
from django.conf.urls import *;
from Rail.views import *
from Rail.admin import *



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voith_sales.views.home', name='home'),
    # url(r'^voith_sales/', include('voith_sales.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^index/', include(admin.site.urls)),
    url(r'^index/', include(mysite.urls)),
    
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name="static"),

)
