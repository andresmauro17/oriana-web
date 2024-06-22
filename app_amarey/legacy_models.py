-----------dev ------------
BASE_DIR /app
STATIC_URL /static/
STATICFILES_DIRS [PosixPath('/app/static')]
STATIC_ROOT /app/static_cdn/static_root
MEDIA_ROOT  /app/media
MEDIA_URL /media/
-----------------------
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Certificados(models.Model):
    neveraid = models.ForeignKey('Nevera', models.DO_NOTHING, db_column='neveraId')  # Field name made lowercase.
    url = models.CharField(max_length=255)
    fechacalibracion = models.DateField(db_column='fechaCalibracion')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificados'


class Companias(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companias'


class Config(models.Model):
    max = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class Correos(models.Model):
    id_correo = models.AutoField(primary_key=True)
    nevera_idnevera = models.ForeignKey('Nevera', models.DO_NOTHING, db_column='nevera_idNevera')  # Field name made lowercase.
    mail = models.CharField(max_length=255)
    activo = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correos'


class Datos(models.Model):
    iddatos = models.AutoField(db_column='idDatos', primary_key=True)  # Field name made lowercase.
    nevera_idnevera = models.ForeignKey('Nevera', models.DO_NOTHING, db_column='nevera_idNevera')  # Field name made lowercase.
    hora = models.TimeField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    temperatura = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    humedad = models.FloatField(blank=True, null=True)
    energia = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos'


class Datostemp(models.Model):
    iddatos = models.AutoField(db_column='idDatos', primary_key=True)  # Field name made lowercase.
    nevera_idnevera = models.ForeignKey('Nevera', models.DO_NOTHING, db_column='nevera_idNevera')  # Field name made lowercase.
    hora = models.TimeField()
    fecha = models.DateField()
    temperatura = models.DecimalField(max_digits=8, decimal_places=2)
    humedad = models.FloatField()
    energia = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosTemp'


class Datostemp2021(models.Model):
    iddatos = models.PositiveIntegerField(db_column='idDatos')  # Field name made lowercase.
    nevera_idnevera = models.PositiveIntegerField(db_column='nevera_idNevera')  # Field name made lowercase.
    hora = models.TimeField()
    fecha = models.DateField()
    temperatura = models.DecimalField(max_digits=8, decimal_places=2)
    humedad = models.FloatField()
    energia = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosTemp2021'


class Empresa(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    compania = models.ForeignKey(Companias, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Informe(models.Model):
    idinforme = models.AutoField(db_column='idInforme', primary_key=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.TimeField(db_column='horaFin', blank=True, null=True)  # Field name made lowercase.
    tempmax = models.FloatField(db_column='tempMax', blank=True, null=True)  # Field name made lowercase.
    tempmin = models.FloatField(db_column='tempMin', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dato = models.ForeignKey(Datos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informe'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Nevera(models.Model):
    idnevera = models.AutoField(db_column='idNevera', primary_key=True)  # Field name made lowercase.
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    cuidad = models.CharField(max_length=255, blank=True, null=True)
    nombrenevera = models.CharField(db_column='nombreNevera', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sensor = models.CharField(max_length=255, blank=True, null=True)
    activa = models.IntegerField(blank=True, null=True)
    modificado = models.IntegerField(blank=True, null=True)
    temmax = models.FloatField(db_column='temMax', blank=True, null=True)  # Field name made lowercase.
    temmin = models.FloatField(db_column='temMin', blank=True, null=True)  # Field name made lowercase.
    humemax = models.FloatField(db_column='humeMax', blank=True, null=True)  # Field name made lowercase.
    humemin = models.FloatField(db_column='humeMin', blank=True, null=True)  # Field name made lowercase.
    telefonomarcado = models.CharField(db_column='telefonoMarcado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefonomarcadob = models.CharField(db_column='telefonoMarcadoB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefonomarcadoc = models.CharField(db_column='telefonoMarcadoC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefonomarcadod = models.CharField(db_column='telefonoMarcadoD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fechacalificacion = models.DateField(db_column='fechaCalificacion', blank=True, null=True)  # Field name made lowercase.
    nombretecnico = models.CharField(db_column='nombreTecnico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    capacidad = models.CharField(max_length=255, blank=True, null=True)
    ciudadcompra = models.CharField(db_column='ciudadCompra', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechacompra = models.DateField(db_column='fechaCompra', blank=True, null=True)  # Field name made lowercase.
    fases = models.CharField(max_length=255, blank=True, null=True)
    voltaje = models.CharField(max_length=255, blank=True, null=True)
    amperaje = models.CharField(max_length=255, blank=True, null=True)
    marcaunidad = models.CharField(db_column='marcaUnidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refunidad = models.CharField(db_column='refUnidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refrigerante = models.CharField(max_length=255, blank=True, null=True)
    periodicidad = models.CharField(max_length=255, blank=True, null=True)
    tipodecontrolador = models.CharField(db_column='tipoDeControlador', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcontrolador = models.CharField(db_column='refControlador', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patroncalibracion = models.CharField(db_column='patronCalibracion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ultimacalibracion = models.DateField(db_column='ultimaCalibracion', blank=True, null=True)  # Field name made lowercase.
    actualizando = models.IntegerField(blank=True, null=True)
    potencia = models.CharField(max_length=255, blank=True, null=True)
    numactivo = models.CharField(db_column='numActivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiponevera = models.CharField(db_column='tipoNevera', max_length=255, blank=True, null=True)  # Field name made lowercase.
    compresor = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tiposensor = models.CharField(db_column='tipoSensor', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ultimodato = models.DecimalField(db_column='ultimoDato', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ultimodatoenergia = models.IntegerField(db_column='ultimoDatoEnergia', blank=True, null=True)  # Field name made lowercase.
    ultimodatohora = models.TimeField(db_column='ultimoDatoHora', blank=True, null=True)  # Field name made lowercase.
    ultimodatofecha = models.DateField(db_column='ultimoDatoFecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nevera'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Registros(models.Model):
    usuario = models.ForeignKey('Users', models.DO_NOTHING)
    sensor = models.ForeignKey(Nevera, models.DO_NOTHING)
    nombre_usuario = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registros'


class Reporte(models.Model):
    nevera_idnevera = models.ForeignKey(Nevera, models.DO_NOTHING, db_column='nevera_idNevera')  # Field name made lowercase.
    hora = models.TimeField()
    fecha = models.DateField()
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporte'


class Sensor(models.Model):
    idsensor = models.AutoField(db_column='idSensor', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    identificador = models.CharField(max_length=255)
    calibradopor = models.CharField(db_column='calibradoPor', max_length=255)  # Field name made lowercase.
    certificado = models.CharField(max_length=255)
    fechacalibracion = models.DateField(db_column='fechaCalibracion')  # Field name made lowercase.
    proxcalibracion = models.DateField(db_column='proxCalibracion')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'


class Sesion(models.Model):
    idsesion = models.AutoField(db_column='idSesion', primary_key=True)  # Field name made lowercase.
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    usuarios_idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_idUsuarios')  # Field name made lowercase.
    usuarios_tipo = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='usuarios_tipo')
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesion'


class Tipousuario(models.Model):
    idtipousuario = models.AutoField(db_column='idTipoUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoUsuario'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    tipousuario = models.IntegerField(db_column='tipoUsuario')  # Field name made lowercase.
    compania = models.ForeignKey(Companias, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Usuarios(models.Model):
    idusuarios = models.AutoField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    tipo = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
