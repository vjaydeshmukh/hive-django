from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/switch-user/(?P<username>.+)', 'hive.admin_utils.switch_user',
        name='switch_user'),
    url(r'^admin/switch-user-back', 'hive.admin_utils.switch_user_back',
        name='switch_user_back'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hive.account_urls')),
    url(r'^mentoring/', include('mentoring.urls')),
    url(r'^cityblogs/', include('cityblogs.urls')),
    url(r'^faq/', 'django.contrib.flatpages.views.flatpage',
        {'url': '/faq/'}, name='faq'),
)

if 'minigroup_digestif' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^minigroup_digestif/', include('minigroup_digestif.urls')),
    )

if 'discourse_sso' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^discourse_sso/', include('discourse_sso.urls'))
    )

urlpatterns += patterns('',
    url(r'', include('directory.urls')),
)
