from django.conf.urls import patterns, include, url
from views import PDPlanCreateView

urlpatterns = patterns('',

    url(r'^$', 'core.views.base', name='base'),
    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^profile/$', 'core.views.profile', name='profile'),
    url(r'^create_pdplan/$', PDPlanCreateView.as_view()),
)
