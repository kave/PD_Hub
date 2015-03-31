from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
#site header name
admin.site.site_header = "PD Hub Administration"
#site title name
admin.site.site_title = "PD Hub"


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls', namespace='core')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^comments/', include('django_comments.urls')),

)