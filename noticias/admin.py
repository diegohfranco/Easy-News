from noticias.models import Noticia , Editoria
from django.contrib import admin

class NoticiaAdmin(admin.ModelAdmin):
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

	fieldsets = [
		('Datas', {'fields': ['data_entrada','data_saida'], 'classes': ['collapse']}),
        (None,               {'fields': ['chapeu','titulo','resumo','texto','editoria']})
        
    ]
	list_display = ('titulo', 'data_entrada','view','usuario')
	list_filter = ['data_entrada']
	search_fields = ['titulo']
	date_hierarchy = 'data_entrada'

	#pega o id do usuario pra salvar na tabela
	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

class EditoriaAdmin(admin.ModelAdmin):
	fields = ['titulo','sub_titulo','imagem_p']
	list_display = ('titulo', 'data_cadastro')
	list_filter = ['data_cadastro']
	search_fields = ['titulo']
	date_hierarchy = 'data_cadastro'
	
admin.site.register(Editoria,EditoriaAdmin)
admin.site.register(Noticia,NoticiaAdmin	)

