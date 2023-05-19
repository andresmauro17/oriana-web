# django imports
from django.db import models
from config.utils.models import CustomBaseModel

# local imports
from app_sensors.models import Sensor

class Data(CustomBaseModel):
    """ data sensor Models.
        This model data measurements in the sensors
    """
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE, db_index=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    energy = models.BooleanField(null=True, blank=True)
    date_time = models.DateTimeField()


    # $table->increments('idDatos');
    # $table->integer('nevera_idNevera')->unsigned();
    # $table->time('hora')->nullable();
    # $table->date('fecha')->nullable();
    # $table->decimal('temperatura', 4,2)->nullable();
    # $table->float('humedad', 8,2)->nullable();
    # $table->tinyInteger('energia')->nullable();
    # $table->timestamps();

    # $table->foreign('nevera_idNevera')->references('idNevera')->on('nevera')->onUpdate('cascade')->onDelete('cascade');
