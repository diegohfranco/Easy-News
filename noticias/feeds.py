from django.contrib.syndication.feeds import Feed
from models import Noticia

class UltimasNoticias(Feed):
	title = 'Easy News - Ultimas'
	link = '/'
	description = "Rss das Ultimas noticias"
	
	def items(self):
		return Noticia.objects.order_by('-data_entrada')[:5]
		
	def item_link(self, noticia):
		return '/noticia/%d/'%noticia.id


class MaisVistas(Feed):
	title = 'Easy News Rss'
	link = '/'
	description = "Easy News - Mais Vistas"
	
	def items(self):
		return Noticia.objects.order_by('-data_entrada')[:5]
		
	def item_link(self, noticia):
		return '/noticia/%d/'%noticia.id
