from enquetes.models import Enquete
from django.contrib import admin
from enquetes.models import Escolha

class EscolhaInline(admin.TabularInline):
    model = Escolha
    extra = 5

class EnqueteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['questao']}),
        ('Date information', {'fields': ['data_entrada'], 'classes': ['collapse']}),
    ]
    inlines = [EscolhaInline]
    #perzonalized list
    list_display = ('questao', 'data_entrada')
    #filtros de lista
    list_filter = ['data_entrada']
    search_fields = ['questao']
    date_hierarchy = 'data_entrada'
    

admin.site.register(Enquete, EnqueteAdmin)
