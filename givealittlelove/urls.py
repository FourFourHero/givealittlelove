from django.conf.urls import patterns, include, url
from django.contrib import admin
from givealittlelove import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/sandbox/home$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'home.html'}),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)