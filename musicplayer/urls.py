from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musicplayer.views.home', name='home'),
    # url(r'^musicplayer/', include('musicplayer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^playlist/$', 'songs.views.playlists'),
    url(r'^playlist/(?P<playlist_id>\d+)/$', 'songs.views.playlist'),
    url(r'^playlist/(?P<playlist_id>\d+)/json$', 'songs.views.playlist_json'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
