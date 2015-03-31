from django.conf.urls import patterns, include, url
from core.views import PDPlanList

urlpatterns = patterns('',

    
    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^profile/$', 'core.views.profile', name='profile'),
    url(r'^$', PDPlanList.as_view()),
)
