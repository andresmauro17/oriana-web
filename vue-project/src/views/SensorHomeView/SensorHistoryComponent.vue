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
      <div class="container">
        <div class="row mt-3">
          <div class="col-sm-12 col-md-6 mb-2">
            <h6 class="surtitle">Rango de fechas</h6>
            <date-picker
              v-model:value="dateRange"
              value-type="format"
              format="YYYY-MM-DD"
              :shortcuts="datePickerShortcuts"
              type="date"
              range
              placeholder="Seleccione el rango de fechas"
            ></date-picker>
          </div>
          <div class="col-sm-12 col-md-6 text-end d-flex align-items-end justify-content-end">
            <input v-if="profileStore.currentuser.is_staff" type="checkbox" id="checkbox" v-model="symbolschecked" />
            <a href="javascript:;" @click="getDataByDate" class="mb-0 mx-2 btn btn-md bg-gradient-primary">
              <i class="fas fa-chart-line "></i> 
              Buscar
            </a>
            <a href="javascript:;" @click="downloadChartDataAsCSV" class="mb-0 mx-2 btn btn-md bg-gradient-success">
              <i class="fas fa-file-excel "></i>
              Excel
            </a>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-sm-12 text-center">
            <h6 class="surtitle">Intervalo</h6>
          </div>
          <div class="col-sm-12 d-flex justify-content-center gap-2">
              <argon-radio :checked="interval=='none'" @click="setRadio('none')">Ningunos</argon-radio>
              <argon-radio :checked="interval=='hourly'" @click="setRadio('hourly')">Por Horas</argon-radio>
              <argon-radio :checked="interval=='time'" @click="setRadio('time')">Un dato diario</argon-radio>
              <argon-radio :checked="interval=='time1&time2'" @click="setRadio('time1&time2')">Dos datos diarios</argon-radio>
            </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-sm-16 col-md-3" v-if="interval=='time' || interval=='time1&time2'">
            <label class="form-label mt-2">Dato 1 (hora)</label>
            <select
              id="choices-gender"
              class="form-control"
              name="choices-gender"
              v-model="time1"
            >
              <option value="07:00:00">7am</option>
              <option value="08:00:00">8am</option>
              <option value="09:00:00">9am</option>
              <option value="10:00:00">10am</option>
              <option value="11:00:00">11am</option>
              <option value="12:00:00">12pm</option>
              <option value="13:00:00">1pm</option>
              <option value="14:00:00">2pm</option>
              <option value="15:00:00">3pm</option>
              <option value="16:00:00">4pm</option>
              <option value="17:00:00">5pm</option>
              <option value="18:00:00">6pm</option>
            </select>
          </div>
          <div class="col-sm-6 col-md-3" v-if="interval=='time1&time2'">
            <label class="form-label mt-2">Dato 2 (hora)</label>
            <select
              id="choices-gender"
              class="form-control"
              name="choices-gender"
              v-model="time2"
            >
              <option value="07:00:00">7am</option>
              <option value="08:00:00">8am</option>
              <option value="09:00:00">9am</option>
              <option value="10:00:00">10am</option>
              <option value="11:00:00">11am</option>
              <option value="12:00:00">12pm</option>
              <option value="13:00:00">1pm</option>
              <option value="14:00:00">2pm</option>
              <option value="15:00:00">3pm</option>
              <option value="16:00:00">4pm</option>
              <option value="17:00:00">5pm</option>
              <option value="18:00:00">6pm</option>
            </select>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6 col-md-3 text-center"><b>Min: </b>{{min_value}}</div>
        <div class="col-sm-6 col-md-3 text-center"><b>Max: </b>{{max_value}}</div>
        <div class="col-sm-6 col-md-3 text-center"><b>Promedio :</b>{{average_value}}</div>
        <div class="col-sm-6 col-md-3 text-center"><b>Cantidad: </b>{{count_value}}</div>
      </div>
      <div class="mt-4">
        <div v-if="showChart" id="mainchart"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps, onMounted, watch } from 'vue';
  import * as echarts from 'echarts';
  import DatePicker from 'vue-datepicker-next';
  import 'vue-datepicker-next/index.css';
  import sensorDataChartOptions from "./sensorDataChartOptions.js"
  import SensorService from "@/services/sensorservice.js"
  import useProfileStore from "@/stores/profile.js"
  import ArgonRadio from "@/components/ArgonRadio.vue";

  const props = defineProps(["sensorData"])
  const profileStore = useProfileStore()
  const symbolschecked = ref(false);

  // ---------- chart logic --------------------
  
  const values = ref([]);
  const values_datetime = ref([]);

  let variableText = "";
  let variableSimbol = "";
  const setInitialOptions = ()=>{
    variableText = props.sensorData.sensor_type=='TEMPERATURE'?"Temperatura":props.sensorData.sensor_type=="HUMIDITY"?"Humedad":"valor";
    variableSimbol = props.sensorData.sensor_type=='TEMPERATURE'?"°C":props.sensorData.sensor_type=="HUMIDITY"?"°C":"";
    
    sensorDataChartOptions.yAxis.axisLabel.formatter = `{value} ${variableSimbol}`;

    sensorDataChartOptions.title.text = `${variableText}: ${props.sensorData.name}`
    sensorDataChartOptions.series[0].name = `${variableText}`
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

  var sensorChart = null;
  const generateChart = ()=>{
    var chartDom = document.getElementById('mainchart');
    if (sensorChart) {
      sensorChart.clear();
      sensorChart.dispose();
    }
    sensorChart = echarts.init(chartDom);
    const chartData = values_datetime.value.map((datetime, index) => [datetime, values.value[index]]);
    sensorDataChartOptions.series[0].data = chartData;
    
    sensorDataChartOptions.graphic=[]
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


  const min_value = ref(null);
  const max_value = ref(null);
  const average_value = ref(null);
  const count_value = ref(0);

  let rawdata = [];
  const showDownloadCsvButton = ref(false);
  const getDataByDate = ()=>{
    showDownloadCsvButton.value = false;
    console.log("isHourly", isHourly.value)
    SensorService.getSensorData(props.sensorData.id, props.sensorData.legacy, dateRange.value[0], dateRange.value[1], isHourly.value, time1.value, time2.value).then((res)=>{
      rawdata = res.data;
      min_value.value = null;
      max_value.value = null;
      average_value.value = null;
      count_value.value = 0;
      
      if(rawdata.length > 0){
        showDownloadCsvButton.value = true;
        min_value.value = Math.min(...rawdata.map(item => item.value));
        max_value.value = Math.max(...rawdata.map(item => item.value));
        average_value.value = (rawdata.reduce((acc, item) => acc + item.value, 0) / rawdata.length).toFixed(2);
        count_value.value = rawdata.length;
      }
      values.value = rawdata.map(item => item.value);
      values_datetime.value = rawdata.map(item => new Date(`${item.date}T${item.time}`));
      generateChart();
    })
  }

  const showChart = ref(true);
  let timer = null;
  window.addEventListener("resize", () => {
    showChart.value = false;
    clearTimeout(timer);
    timer = setTimeout(() => {
      showChart.value = true;
    }, 600);
  });

  watch(showChart, (newValue) => {
    if (newValue) {
      setTimeout(() => {
        generateChart();
      }, 600);
    }
  });


  // ---------- download logic --------------------
  function downloadChartDataAsCSV() {
    if (!rawdata.length) {
        alert("No data available for download!");
        return;
    }

    let csvContent = `dato;fecha;valor;hora;energia;unidad;reporte\n`;

    rawdata.forEach(item => {
        const { id, date, time, value, energy } = item;
        csvContent += `${id};${date};${value};${time};${energy ? "Si" : "No"};${variableSimbol};\n`;
    });

    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `reporte_${props.sensorData.name}.csv`;
    document.body.appendChild(a);
    a.click();
    
    // Cleanup
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
  }

  // ---------- times logic --------------------

  let time1 = ref(null);
  let time2 = ref(null);

  // ---------- radio logic --------------------
  const interval = ref("none");
  const isHourly = ref(false);
  const setRadio = (option)=>{
    interval.value = option;
    isHourly.value = false;
    if (interval.value == "hourly"){
      isHourly.value = true;
    }
  }

  watch(interval, (newValue) => {
    if (newValue == "time") {
      time1.value = "07:00:00";
      time2.value = null;
    } else if (newValue == "time1&time2") {
      time1.value = "07:00:00";
      time2.value = "17:00:00";
    }
  });

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
      text:'semana anterior',
      onClick() {
        let date = new Date();
        let day = date.getDay();

        // Calculate the difference to the nearest Monday
        let diffToMonday = (day === 0 ? -6 : 1) - day;

        // Calculate the first day of the current week (Monday)
        let firstDayOfWeek = new Date(date);
        firstDayOfWeek.setDate(date.getDate() + diffToMonday - 7);

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
      text: 'Mes anterior',
      onClick() {
        let date = new Date();
        let firstDay = new Date(date.getFullYear(), date.getMonth() - 1, 1);
        let lastDay = new Date(date.getFullYear(), date.getMonth(), 0);
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
      text: 'Trimestre anterior',
      onClick() {
        let date = new Date();
        let quarter = Math.floor(date.getMonth() / 3) + 1;
        let firstDayOfQuarter = new Date(date.getFullYear(), (quarter - 1) * 3, 1);
        let lastDayOfQuarter = new Date(date.getFullYear(), quarter * 3, 0);
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
    {
      text: 'Año aterior',
      onClick() {
        let date = new Date();
        let firstDay = new Date(date.getFullYear() - 1, 0, 1);
        let lastDay = new Date(date.getFullYear() - 1, 11, 31);
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