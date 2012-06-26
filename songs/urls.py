from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musicplayer.views.home', name='home'),
    # url(r'^musicplayer/', include('musicplayer.foo.urls')),
    url(r'^playlists', 'songs.views.playlists'),
)