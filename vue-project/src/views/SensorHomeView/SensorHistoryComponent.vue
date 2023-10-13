<template>
  <div class="card z-index-2">
    <!-- Card header -->
    <div class="card-header py-3 d-flex align-items-center border-bottom">
        <div class="d-flex align-items-center">
          <!-- Title -->
          <!-- <h5 class="text-capitalize">{{ sensorData.name }}</h5> -->
          <!-- Surtitle -->
          <h6 class="surtitle">Historial de datos</h6>
        </div>
        
        <div class="text-end ms-auto">
          <a :href="`/sensors/${sensorData.id}/edit`" class="mb-0 btn btn-xs bg-neutral">
            <i class="fas fa-cog "></i> 
            Config
          </a>
        </div>
    </div>

    <div class="p-3 card-body">
      <date-picker
        v-model:value="dateRange"
        value-type="format"
        format="YYYY-MM-DD"
        :shortcuts="datePickerShortcuts"
        type="date"
        range
        placeholder="Seleccione el rango de fechas"
      ></date-picker>
      <a href="javascript:;" @click="getDataByDate" class="mb-0 mx-2 btn btn-md bg-gradient-success">
        <i class="fas fa-chart-line "></i> 
        Buscar
      </a>
      <!-- <a
            class="mt-4 btn btn-sm"
            :href="actions.route"
            :class="`bg-gradient-${actions.color}`"
          >
            {{ actions.label }}
          </a> -->
      <div class="mt-4">
        <div id="mainchart"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps, onMounted } from 'vue';
  import * as echarts from 'echarts';
  import DatePicker from 'vue-datepicker-next';
  import 'vue-datepicker-next/index.css';
  import sensorDataChartOptions from "./sensorDataChartOptions.js"
  import SensorService from "@/services/sensorservice.js"

  const props = defineProps(["sensorData"])

  const setInitialOptions = ()=>{
    let variable = props.sensorData.sensor_type=='TEMPERATURE'?"Temperatura":props.sensorData.sensor_type=="HUMIDITY"?"Humedad":"valor";
    sensorDataChartOptions.title.text = `${variable}: ${props.sensorData.name}`
    sensorDataChartOptions.series[0].name = `${variable}`
  }
  const generateChart = ()=>{
    var chartDom = document.getElementById('mainchart');
    var sensorChart = echarts.init(chartDom);
    sensorDataChartOptions.series[0].data = values.value
    sensorDataChartOptions.xAxis.data = values_datetime.value
    
    if (sensorDataChartOptions.series[0].data.length === 0) {
      sensorDataChartOptions.graphic = [
        {
          type: 'text',
          left: 'center',
          top: 'center',
          style: {
            fill: 'rgba(0, 0, 0, 0.25)',
            fontSize: 18,
            fontWeight: 'bold',
            text: `⚠️ No hay datos disponibles entre ${dateRange.value[0]} y ${dateRange.value[1]}`
          }
        }
      ];
    }
    sensorChart.setOption(sensorDataChartOptions)
  };

  const getDataByDate = ()=>{
    SensorService.getSensorData(props.sensorData.id, dateRange.value[0], dateRange.value[1]).then((res)=>{
      let rawdata = res.data;
      values.value = rawdata.map(item => item.value);
      values_datetime.value = rawdata.map(item => item.date_time);
      generateChart();
    })
  }

  const values = ref([]);
  const values_datetime = ref([]);
  onMounted(()=>{
    setInitialOptions()
    getDataByDate()
  })

  const currentDate = new Date();

  const year = currentDate.getFullYear();
  const month = String(currentDate.getMonth() + 1).padStart(2, '0');
  const day = String(currentDate.getDate()).padStart(2, '0');

  const formattedDateToday = `${year}-${month}-${day}`;

  const dateRange = ref([formattedDateToday, formattedDateToday]);
  const datePickerShortcuts = ref([
    {
      text: 'hoy',
      onClick() {
        const date = new Date();
        // return a Date
        return date;
      },
    },
    {
      text: 'Ayer',
      onClick() {
        const date = new Date();
        date.setTime(date.getTime() - 3600 * 1000 * 24);
        return date;
      },
    },
    {
      text: 'Este mes',
      onClick() {
        const date = new Date();
        date.setTime(date.getTime() - 3600 * 1000 * 24);
        return date;
      },
    },
    {
      text: 'Este trimestre',
      onClick() {
        const date = new Date();
        date.setTime(date.getTime() - 3600 * 1000 * 24);
        return date;
      },
    },
  ])

</script>

<style lang="css" scoped>
#mainchart{
  width: 100%;
  height:600px;
}
</style>