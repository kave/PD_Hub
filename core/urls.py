from django.conf.urls import patterns, include, url
from core.views import *

urlpatterns = patterns('',


    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^create_pdplan/$', PDPlanCreateView.as_view()),
    url(r'^$', PDPlanList.as_view()),
    url(r'^profile/$', PDPlanList.as_view(), name='profile'),
    url(r'^list/$', PDPlanList.as_view(), name='pdp_list'),
    url(r'^view/(?P<pk>\d+)/$', PDPPlanDetailView.as_view(), name='pdp_view'),
)
