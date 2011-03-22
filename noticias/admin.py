from noticias.models import Noticia
from django.contrib import admin

#from polls.models import Choice

#class ChoiceInline(admin.TabularInline):
    #model = Choice
    #extra = 3

class NoticiaAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['chapeu','titulo','resumo','texto','view','slug']}),
        ('Datas', {'fields': ['data_entrada','data_saida'], 'classes': ['collapse']})
    ]
    #inlines = [ChoiceInline]
    #perzonalized list
	list_display = ('titulo', 'data_entrada')
	#filtros de lista
	list_filter = ['data_entrada']
	search_fields = ['titulo']
	date_hierarchy = 'data_entrada'
	
admin.site.register(Noticia, NoticiaAdmin)

