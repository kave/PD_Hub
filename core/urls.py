from django.conf.urls import patterns, include, url
from core.views import *

urlpatterns = patterns('',
    url(r'^$', 'core.views.base', name='base'),
    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^profile/$', 'core.views.profile', name='profile'),
    url(r'^create_pdplan/$', PDPlanCreateView.as_view(), name='pdp_create'),
    url(r'^list/$', PDPlanList.as_view(), name='pdp_list'),
    url(r'^view/(?P<pk>\d+)/$', PDPlanDetailView.as_view(), name='pdp_view'),
    url(r'^clone/(?P<plan_id>\d+)/$', PDPlanClone.as_view(), name='clone'),
)
