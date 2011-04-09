from django.conf.urls.defaults import *
from django.conf import settings
from noticias.feeds import UltimasNoticias , MaisVistas
from enquetes.models import Enquete

from django.contrib import admin
admin.autodiscover()

feeds = {
    'ultimas': UltimasNoticias,
    'maisvistas': MaisVistas,
}

info_dict = {
    'queryset': Enquete.objects.all(),
}

urlpatterns = patterns('',
	#index
	(r'^$', 'noticias.views.index'),
	
	#noticia
	(r'^noticias/(?P<slug>[\w_-]+)/$', 'noticias.views.detail'),
	(r'^noticias/', 'noticias.views.index'),
	
	#rss
	(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),	

    #admin:
    (r'^admin/', include(admin.site.urls)),

	#contato	
	(r'^contato/$', 'views.contato'),
	
	#galerias
	(r'^galeria/$', 'galeria.views.albuns'),
	(r'^galeria/(?P<slug>[\w_-]+)/$', 'galeria.views.album'),
	(r'^galeria/imagem/(?P<slug>[\w_-]+)/$', 'galeria.views.imagem'),
	
	
	#enquetes
	(r'^enquetes/$', 'django.views.generic.list_detail.object_list', info_dict),
	(r'^enquetes/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
	url(r'^enquetes/(?P<object_id>\d+)/resultado/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, 							template_name='enquetes/enquete_results.html'), 'enquete_results'),
    (r'^enquetes/(?P<enquete_id>\d+)/vote/$', 'enquetes.views.vote'),


	# Static media (serve using real web server when in production)
  	(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
  	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),
)

#somente se for em ambiente de desenvolvimento
if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
