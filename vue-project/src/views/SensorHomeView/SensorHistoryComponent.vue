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
        :shortcuts="datePickerShortcuts"
        type="date"
        range
        placeholder="Seleccione el rango de fechas"
      ></date-picker>
      <div class="mt-4">
        <div id="mainchart" style="width: 1000px;height:600px;"></div>
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

  const generateChart = ()=>{
    var chartDom = document.getElementById('mainchart');
    var sensorChart = echarts.init(chartDom);
    sensorDataChartOptions.series[0].data = values.value
    sensorDataChartOptions.xAxis.data = values_datetime.value
    console.log("setoptions:", sensorDataChartOptions)
    sensorChart.setOption(sensorDataChartOptions)
  };

  const values = ref([]);
  const values_datetime = ref([]);
  onMounted(()=>{
    SensorService.getSensorData(props.sensorData.id).then((res)=>{
      let rawdata = res.data;
      values.value = rawdata.map(item => item.value);
      values_datetime.value = rawdata.map(item => item.date_time);
      console.log("values:", values.value);
      generateChart();
    })
  })

  const dateRange = ref([new Date(), new Date()]);
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

<style lang="scss" scoped>

</style>