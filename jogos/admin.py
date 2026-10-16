from django.contrib import admin
from .models import Modalidade, Atleta, Equipe, Tecnico


# Register your models here.
@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ["nome", "matricula", "equipe"]
    list_filter = ["equipe", "modalidade"]
    search_fields = ["nome"]


class TecnicoTabularInLine(admin.TabularInline):
    model = Tecnico


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ["nome", "curso", "quantidade_atletas"]
    inlines = [TecnicoTabularInLine]

admin.site.register(Modalidade)