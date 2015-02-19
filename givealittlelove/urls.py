from django.conf.urls import patterns, include, url
from django.contrib import admin
from givealittlelove import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/sandbox/home$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'home.html'}),

    # API
    # API AMBASSADOR
    url(r'^api/sandbox/ambassador/create$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'ambassador_create.html'}),
    url(r'^api/ambassador/create', 'givealittlelove.gall.views.ambassador.create'),
    # API ACTIVATION
    url(r'^api/sandbox/activation/create$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'activation_create.html'}),
    url(r'^api/activation/create', 'givealittlelove.gall.views.activation.create'),
    url(r'^api/sandbox/activation/get-by-code$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'activation_getbycode.html'}),
    url(r'^api/activation/get-by-code', 'givealittlelove.gall.views.activation.get_by_code'),
    # API COUPON
    url(r'^api/sandbox/coupon/create$', 'givealittlelove.gall.views.apisandbox.show', {'template_name':'coupon_create.html'}),
    url(r'^api/coupon/create', 'givealittlelove.gall.views.coupon.create'),

)



urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)