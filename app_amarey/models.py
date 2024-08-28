""" Amarey legacy models """
import random
from datetime import datetime, time
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save

from app_utilities.utils import get_filename_ext

class Companias(models.Model):
    """ Legacy Companias model """
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        """ Meta class """
        app_label = "app_amarey"
        managed = False
        db_table = "companias"


class Empresa(models.Model):
    """ Legacy Empresa model """
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    compania = models.ForeignKey(
        Companias, models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        """ Meta class """
        app_label = "app_amarey"
        managed = False
        db_table = "empresa"


class Datos(models.Model):
    """ Datos legacy model"""
    iddatos = models.AutoField(
        db_column="idDatos", primary_key=True
    )  # Field name made lowercase.
    nevera = models.ForeignKey(
        "Nevera",
        models.DO_NOTHING,
        related_name="datos",
        db_column="nevera_idNevera",
    )  # Field name made lowercase.
    hora = models.TimeField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    temperatura = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    humedad = models.FloatField(blank=True, null=True)
    energia = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        """ Meta class """
        app_label = "app_amarey"
        managed = False
        db_table = "datos"


class NeveraQuerySet(models.query.QuerySet):
    """ queryset """
    def get_active(self):
        """ get active nevera"""
        return self.filter(Q(activa=1) | Q(activa=4))


class NeveraManager(models.Manager):
    """ NeveraManager """
    def get_queryset(self):
        """ get queryset """
        return NeveraQuerySet(self.model, using=self._db)

    def get_active(self):
        """ get active """
        return self.get_queryset().get_active()


class Nevera(models.Model):
    """ legacy nevera model """
    TIPO_SENSOR_CHOICES = (
        ("temperatura", "temperatura"),
        ("humedad", "humedad"),
    )
    idnevera = models.AutoField(
        db_column="idNevera", primary_key=True
    )  # Field name made lowercase.
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    cuidad = models.CharField(max_length=255, null=True)
    nombrenevera = models.CharField(
        db_column="nombreNevera", max_length=255, null=True
    )  # Field name made lowercase.
    sensor = models.CharField(max_length=255, null=True, blank=True)
    activa = models.IntegerField(null=True)
    modificado = models.IntegerField(null=True)
    temmax = models.FloatField(
        db_column="temMax", default=8, null=True
    )  # Field name made lowercase.
    temmin = models.FloatField(
        db_column="temMin", default=2, null=True
    )  # Field name made lowercase.
    humemax = models.FloatField(
        db_column="humeMax", blank=True, null=True
    )  # Field name made lowercase.
    humemin = models.FloatField(
        db_column="humeMin", blank=True, null=True
    )  # Field name made lowercase.
    telefonomarcado = models.CharField(
        db_column="telefonoMarcado", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    telefonomarcadob = models.CharField(
        db_column="telefonoMarcadoB", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    telefonomarcadoc = models.CharField(
        db_column="telefonoMarcadoC", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    telefonomarcadod = models.CharField(
        db_column="telefonoMarcadoD", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fechacalificacion = models.DateField(
        db_column="fechaCalificacion", blank=True, null=True
    )  # Field name made lowercase.
    nombretecnico = models.CharField(
        db_column="nombreTecnico", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    notas = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    capacidad = models.CharField(max_length=255, blank=True, null=True)
    ciudadcompra = models.CharField(
        db_column="ciudadCompra", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    fechacompra = models.DateField(
        db_column="fechaCompra", blank=True, null=True
    )  # Field name made lowercase.
    fases = models.CharField(max_length=255, blank=True, null=True)
    voltaje = models.CharField(max_length=255, blank=True, null=True)
    amperaje = models.CharField(max_length=255, blank=True, null=True)
    marcaunidad = models.CharField(
        db_column="marcaUnidad", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    refunidad = models.CharField(
        db_column="refUnidad", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    refrigerante = models.CharField(max_length=255, blank=True, null=True)
    periodicidad = models.CharField(max_length=255, blank=True, null=True)
    tipodecontrolador = models.CharField(
        db_column="tipoDeControlador", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    refcontrolador = models.CharField(
        db_column="refControlador", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    patroncalibracion = models.CharField(
        db_column="patronCalibracion", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    ultimacalibracion = models.DateField(
        db_column="ultimaCalibracion", blank=True, null=True
    )  # Field name made lowercase.
    actualizando = models.IntegerField(blank=True, null=True)
    potencia = models.CharField(max_length=255, blank=True, null=True)
    numactivo = models.CharField(
        db_column="numActivo", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    tiponevera = models.CharField(
        db_column="tipoNevera", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    compresor = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    tiposensor = models.CharField(
        db_column="tipoSensor",
        max_length=11,
        choices=TIPO_SENSOR_CHOICES,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ultimodato = models.DecimalField(
        db_column="ultimoDato",
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ultimodatoenergia = models.IntegerField(
        db_column="ultimoDatoEnergia", blank=True, null=True
    )  # Field name made lowercase.
    ultimodatohora = models.TimeField(
        db_column="ultimoDatoHora", blank=True, null=True
    )  # Field name made lowercase.
    ultimodatofecha = models.DateField(
        db_column="ultimoDatoFecha", blank=True, null=True
    )  # Field name made lowercase.
    objects = NeveraManager()

    @property
    def get_location(self):
        """ Return the emprsa name """
        return f"{self.empresa.nombre}"

    @property
    def ultimodatetime(self):
        """ retunr the last datetime data """
        if self.ultimodatofecha and self.ultimodatohora:
            return datetime.combine(self.ultimodatofecha, self.ultimodatohora)
        return None

    def __str__(self):
        return f"{self.nombrenevera}"

    class Meta:
        """ Meta class """
        app_label = "app_amarey"
        managed = False
        db_table = "nevera"


def nevera_post_save(sender, instance, created, *args, **kwargs):
    """ Signal to create a data after save it """
    if created:
        # Logic to execute only when a new record is created
        current_date = datetime.now().date()
        midnight_time = time(0, 0)
        Datos.objects.create(
            nevera=instance,
            hora=midnight_time,
            fecha=current_date,
            temperatura=0,
            humedad=0,
            energia=1,
        )


post_save.connect(nevera_post_save, sender=Nevera)


def upload_cert_path(instance, filename):
    """ path to store certs """
    rand = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = f"{rand}_{name}{ext}"
    return f"certificates/neveras/{instance.nevera.idnevera}/{final_filename}"


class Certificados(models.Model):
    """calibration certs"""
    nevera = models.ForeignKey(
        "Nevera", models.DO_NOTHING, db_column="neveraId"
    )
    # url = models.CharField(max_length=255)
    url = models.FileField(upload_to=upload_cert_path, max_length=255)
    fechacalibracion = models.DateField(db_column="fechaCalibracion")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        """Meta class"""

        managed = False
        db_table = "certificados"
