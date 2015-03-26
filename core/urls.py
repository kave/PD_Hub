from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'core.views.base', name='base'),
    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^register/$', 'core.views.register', name='register'),
)
