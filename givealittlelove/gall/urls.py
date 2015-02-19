from django.conf.urls import patterns, include, url
from django.contrib import admin
from givealittlelove.gall import views

urlpatterns = patterns('',

    # API SANDBOX
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/sandbox/home$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'home.html'}),
)