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
        <div v-if="profileStore.currentuser.is_staff" class="text-end ms-auto">
          <a :href="`/admin/app_data/data/?sensor__id__exact=${sensorData.id}`" target="blank" class="mb-0 btn btn-xs bg-neutral">
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
      <input v-if="profileStore.currentuser.is_staff" type="checkbox" id="checkbox" v-model="symbolschecked" />
      <!-- <label for="checkbox">sym</label> -->
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
  import useProfileStore from "@/stores/profile.js"

  const props = defineProps(["sensorData"])
  const profileStore = useProfileStore()
  const symbolschecked = ref(false);

  // ---------- chart logic --------------------
  
  const values = ref([]);
  const values_datetime = ref([]);

  const setInitialOptions = ()=>{
    let variable = props.sensorData.sensor_type=='TEMPERATURE'?"Temperatura":props.sensorData.sensor_type=="HUMIDITY"?"Humedad":"valor";
    sensorDataChartOptions.title.text = `${variable}: ${props.sensorData.name}`
    sensorDataChartOptions.series[0].name = `${variable}`
    sensorDataChartOptions.series[0].markLine.data[0].yAxis = props.sensorData.max_threshold
    sensorDataChartOptions.series[0].markLine.data[1].yAxis = props.sensorData.min_threshold

    sensorDataChartOptions.yAxis.min = (value)=>{
      const min_threshold = props.sensorData.min_threshold
      return value.min - 1 > min_threshold ? min_threshold -1 : value.min - 1; // Adjust the min value
    }

    sensorDataChartOptions.yAxis.max = (value)=> {
        const max_threshold = props.sensorData.max_threshold
        return value.max + 1 < max_threshold ? max_threshold + 1 : value.max + 1; // Adjust the max value
    }
  }

  const generateChart = ()=>{
    var chartDom = document.getElementById('mainchart');
    var sensorChart = echarts.init(chartDom);
    const chartData = values_datetime.value.map((datetime, index) => [datetime, values.value[index]]);
    sensorDataChartOptions.series[0].data = chartData;
    
    if (chartData.length === 0) {
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
    if (symbolschecked.value) {
      sensorDataChartOptions.series[0].symbol = 'circle';
    }else{
      sensorDataChartOptions.series[0].symbol = 'none';
    }
    sensorDataChartOptions.dataZoom.startValue = dateRange.value[0];
    sensorChart.setOption(sensorDataChartOptions);
  };

  const getDataByDate = ()=>{
    SensorService.getSensorData(props.sensorData.id, props.sensorData.legacy, dateRange.value[0], dateRange.value[1]).then((res)=>{
      let rawdata = res.data;
      values.value = rawdata.map(item => item.value);
      values_datetime.value = rawdata.map(item => new Date(`${item.date}T${item.time}`));
      generateChart();
    })
  }

  // ---------- Datime picker logic --------------------
  const currentDate = new Date();
  const dateRange = ref([]);
  const formattedDateToday = ref("");

  const formatDate = (dateToformat)=>{
    const year = dateToformat.getFullYear();
    const month = String(dateToformat.getMonth() + 1).padStart(2, '0');
    const day = String(dateToformat.getDate()).padStart(2, '0');

    return `${year}-${month}-${day}`;
  }

  const datePickerShortcuts = ref([
    {
      text: 'hoy',
      onClick() {
        dateRange.value = [formattedDateToday.value, formattedDateToday.value]
      },
    },
    {
      text: 'Ayer',
      onClick() {
        let date = new Date();
        date.setTime(date.getTime() - 3600 * 1000 * 24);
        date = formatDate(date)
        dateRange.value = [date, date]
      },
    },
    {
      text: 'Esta semana',
      onClick() {
        let date = new Date();
        let day = date.getDay();

        // Calculate the difference to the nearest Monday
        let diffToMonday = (day === 0 ? -6 : 1) - day;

        // Calculate the first day of the current week (Monday)
        let firstDayOfWeek = new Date(date);
        firstDayOfWeek.setDate(date.getDate() + diffToMonday);

        // Calculate the last day of the current week (Sunday)
        let lastDayOfWeek = new Date(firstDayOfWeek);
        lastDayOfWeek.setDate(firstDayOfWeek.getDate() + 6);
        
        firstDayOfWeek = formatDate(firstDayOfWeek)
        lastDayOfWeek = formatDate(lastDayOfWeek)
        dateRange.value = [firstDayOfWeek, lastDayOfWeek]
        
      },
    },
    {
      text: 'Este mes',
      onClick() {
        let date = new Date();
        let firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
        let lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
        firstDay = formatDate(firstDay)
        lastDay = formatDate(lastDay)
        dateRange.value = [firstDay, lastDay]
      },
    },
    {
      text: 'Este trimestre',
      onClick() {
        let date = new Date();
        let quarter = Math.floor(date.getMonth() / 3) + 1;
        let firstDayOfQuarter = new Date(date.getFullYear(), (quarter - 1) * 3, 1);
        let lastDayOfQuarter = new Date(date.getFullYear(), quarter * 3, 0);
        // let firstDayOfQuarter = new Date(date.getFullYear(), date.getMonth() - 2, 1);
        // let lastDayOfQuarter = new Date(date.getFullYear(), date.getMonth(), 0);
        firstDayOfQuarter = formatDate(firstDayOfQuarter)
        lastDayOfQuarter = formatDate(lastDayOfQuarter)
        dateRange.value = [firstDayOfQuarter, lastDayOfQuarter]
      },
    },
    {
      text: 'Este año',
      onClick() {
        let date = new Date();
        let firstDay = new Date(date.getFullYear(), 0, 1);
        let lastDay = new Date(date.getFullYear(), 11, 31);
        firstDay = formatDate(firstDay)
        lastDay = formatDate(lastDay)
        dateRange.value = [firstDay, lastDay]
        
      },
    },
  ])

  // ---------- end Datime picker logic --------------------
  // Initializing component
  onMounted(()=>{
    formattedDateToday.value = formatDate(currentDate)
    dateRange.value = [formattedDateToday.value, formattedDateToday.value]
    setInitialOptions()
    getDataByDate()
  })

</script>

<style lang="css" scoped>
#mainchart{
  width: 100%;
  height:600px;
}
</style>