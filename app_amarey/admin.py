""" Admin for the legacy DB """
from django.contrib import admin

# local import
from .models import Companias, Empresa, Nevera, Datos, Certificados


class NeveraInline(admin.TabularInline):
    """NeveraInline"""

    model = Nevera
    extra = 1
    can_delete = True
    show_change_link = True


class DatosInline(admin.StackedInline):
    """DatosInline"""

    model = Datos
    can_delete = True
    show_change_link = True
    extra = 0


class CertificadosInline(admin.TabularInline):
    """CertificadosInline"""

    model = Certificados
    can_delete = True
    show_change_link = True
    extra = 0


@admin.register(Companias)
class CompaniasAdmin(admin.ModelAdmin):
    """CompaniasAdmin"""

    list_display = ["id", "nombre", "created_at", "updated_at"]
    ordering = []


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    """EmpresaAdmin"""

    list_display = ["id", "nombre", "compania", "created_at", "updated_at"]
    ordering = []
    list_filter = ["compania"]
    inlines = [NeveraInline]


class CompaniasFilter(admin.SimpleListFilter):
    """CompaniasFilter"""

    title = "Companias"
    parameter_name = "compania"

    def lookups(self, request, model_admin):
        """adding custom filters"""
        companias = Companias.objects.all()
        return [(compania.id, compania.nombre) for compania in companias]

    def queryset(self, request, queryset):
        """filter querysets"""
        if self.value():
            return queryset.filter(empresa__compania_id=self.value())
        return queryset


@admin.register(Nevera)
class NeveraAdmin(admin.ModelAdmin):
    """NeveraAdmin"""

    exclude = [
        "direccion",
        "fechacalificacion",
        "nombretecnico",
        "marca",
        "modelo",
        "serial",
        "capacidad",
        "ciudadcompra",
        "fechacompra",
        "fases",
        "voltaje",
        "amperaje",
        "marcaunidad",
        "refunidad",
        "refrigerante",
        "periodicidad",
        "tipodecontrolador",
        "refcontrolador",
        "patroncalibracion",
        "potencia",
        "numactivo",
        "tiponevera",
        "compresor",
    ]
    list_display = [
        "idnevera",
        "empresa",
        "cuidad",
        "nombrenevera",
        "sensor",
        "activa",
        "modificado",
        "temmax",
        "temmin",
        "humemax",
        "humemin",
        "telefonomarcado",
        "telefonomarcadob",
        "telefonomarcadoc",
        "telefonomarcadod",
        "tiposensor",
        "ultimodato",
        "ultimodatoenergia",
        "ultimodatohora",
        "ultimodatofecha",
        "updated_at",
    ]
    list_editable = [
        "cuidad",
        "nombrenevera",
        "sensor",
        "activa",
        "modificado",
        "temmax",
        "temmin",
        "humemax",
        "humemin",
        "telefonomarcado",
        "telefonomarcadob",
        "telefonomarcadoc",
        "telefonomarcadod",
        "tiposensor",
    ]
    ordering = ["empresa"]
    list_filter = ["activa", "modificado", CompaniasFilter, "empresa"]
    search_fields = ["sensor", "nombrenevera"]
    inlines = [CertificadosInline]
    save_as = True
    save_on_top = True


@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    """ DatosAdmin """
    list_display = [
        "iddatos",
        "nevera",
        "hora",
        "fecha",
        "temperatura",
        "humedad",
        "energia",
        "created_at",
        "updated_at",
    ]
    ordering = ["iddatos"]
    list_filter = ["nevera"]
