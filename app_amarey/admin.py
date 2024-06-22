from django.contrib import admin

# local import
from .models import Companias, Empresa, Nevera, Datos

class NeveraInline(admin.TabularInline):
    model = Nevera
    extra = 1
    can_delete = True
    show_change_link = True

class DatosInline(admin.StackedInline):
    model = Datos
    can_delete = True
    show_change_link = True

@admin.register(Companias)
class CompaniasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','created_at', 'updated_at']
    ordering = []

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'compania', 'created_at', 'updated_at']
    ordering = []
    list_filter = ['compania']
    inlines = [ NeveraInline ]

class CompaniasFilter(admin.SimpleListFilter):
    title = 'Companias'
    parameter_name = 'compania'

    def lookups(self, request, model_admin):
        companias = Companias.objects.all()
        return [(compania.id, compania.nombre) for compania in companias]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(empresa__compania_id=self.value())
        return queryset



@admin.register(Nevera)
class NeveraAdmin(admin.ModelAdmin):
    list_display = ['idnevera', 'empresa', 'cuidad', 'nombrenevera', 'sensor', 'activa', 'modificado', 'temmax', 'temmin', 'humemax', 'humemin', 'telefonomarcado', 'telefonomarcadob', 'telefonomarcadoc', 'telefonomarcadod', 'tiposensor', 'ultimodato', 'ultimodatoenergia', 'ultimodatohora', 'ultimodatofecha', 'updated_at']
    list_editable = [ 'cuidad', 'nombrenevera', 'sensor', 'activa', 'modificado', 'temmax', 'temmin', 'humemax', 'humemin', 'telefonomarcado', 'telefonomarcadob', 'telefonomarcadoc', 'telefonomarcadod', 'tiposensor',]
    ordering = ['empresa']
    list_filter = [CompaniasFilter, 'activa', 'empresa']
    # inlines = [ DatosInline ]


@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ['iddatos','nevera_idnevera','hora','fecha','temperatura','humedad','energia','created_at','updated_at']
    ordering = []
    list_filter = ['nevera_idnevera']

    