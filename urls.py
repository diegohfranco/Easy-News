from django.conf.urls.defaults import *

from noticias.feeds import UltimasNoticias , MaisVistas

from django.contrib import admin
admin.autodiscover()

feeds = {
    'ultimas': UltimasNoticias,
    'maisvistas': MaisVistas,
}

urlpatterns = patterns('easy_news',
	#index
	(r'^$', 'noticias.views.index'),
	
	#noticia
	(r'^noticias/(?P<noticia_id>\d+)/$', 'noticias.views.detail'),
	(r'^noticias/', 'noticias.views.index'),
	
	#rss
	#(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
	#	{'feed_dict': {'ultimas': UltimasNoticias}}),
	(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),	

	# Static media (serve using real web server when in production)
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        #{'document_root': settings.MEDIA_ROOT}),

    #admin:
    (r'^admin/', include(admin.site.urls)),
)
