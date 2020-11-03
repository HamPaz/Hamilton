from django.contrib import admin
from .models import Pergs, Escol

class EscolInline(admin.TabularInline):
    model = Escol
    extra = 2
class PergsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Perguntas', {'fields': ['txt_perg']}),
        ('Informações da data', {'fields': ['dat_publ'], 'classes': ['collapse']}),
    ]
    inlines = [EscolInline]
    list_display = ('txt_perg', 'dat_publ', 'publicado_recente')
    list_filter = ['dat_publ']
    search_fields = ['txt_perg']
admin.site.register(Pergs, PergsAdmin)
#admin.site.register(Escol, EscolInline)
