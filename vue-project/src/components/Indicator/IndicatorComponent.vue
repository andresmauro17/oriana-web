<template>
  <div class="card">
    <!-- Card header -->
    <div class="card-header py-3 d-flex align-items-center border-bottom">
        <div class="d-flex align-items-center">
          <!-- Title -->
          <div class="mx-3">
            <a href="javascript:;" class="text-md text-dark font-weight-600">{{ sensor.name }}</a>
            <small class="d-block text-muted">{{ sensor.location }}</small>
          </div>
          <!-- <h5 class="text-capitalize">{{ sensor.name }} </h5> -->
          <!-- Surtitle -->
          <!-- <h6 class="text-muted text-small text-end"> {{ sensor.location }} </h6> -->
        </div>
        <div v-if="isRealTimeMode" class="p-3 ms-auto text-center">
          <span class="badge badge-secondary">
            <i class="fas fa-dot-circle recording-text"></i>
            Real time
          </span>
        </div>
        <div v-if="profileStore.currentuser.is_staff" class="text-end ms-auto">
          <a :href="`/admin/app_sensors/sensor/${sensor.id}/change/`" target="blank" class="mb-0 btn btn-xs bg-neutral">
            <i class="fas fa-cog "></i> 
            Config
          </a>
        </div>
    </div>
    <!-- Card body -->
    <a :href="`/sensors/${sensor.id}`">
      <div class="card-body card-body-indicator">
        <div class="push-indicator" :class="colorClass">
          <div class="push-in-indicator">
            <p class="display">
              <span id="temperatura_entero" class="temp_entero"> {{sensor.last_value}}</span>
              <!-- <span id="temperatura_decimal" class="temp_decimal">.5</span> -->
              <span v-if="sensor.sensor_type=='TEMPERATURE'" class="temp_grados">&deg;</span>
              <span v-if="sensor.sensor_type=='HUMIDITY'" class="temp_grados">%</span>
            </p>
          </div>
        </div>
        <h6 class="mt-3 mb-0 font-weight-bolder text-center">{{formatedDatetime}}</h6>
        <p v-if="sensor.last_energy_state==true" class="text-sm mb-0 font-weight-bolder text-center"> <i class="ni ni-check-bold text-success text-sm opacity-10"></i> Energia</p>
        <p v-else-if="sensor.last_energy_state==false" class="text-sm mb-0 font-weight-bolder text-center"> <i class="ni ni-fat-remove text-warning text-sm opacity-10"></i> Energia</p>
        <p v-else class="text-sm mb-0 font-weight-bolder text-center"> ------- </p>
        <!-- <p class="text-sm mb-0 opacity-8 text-center"><span class="badge bg-default">Sensor Desactualizado</span></p>
        <p class="text-sm mb-0 opacity-8 text-center"><i class="ni ni-check-bold text-success text-sm opacity-10"></i> Todo esta ok</p>
        <p class="text-sm mb-0 opacity-8 text-center"><span class="badge bg-warning">Por encima el limite</span></p>
        <p class="text-sm mb-0 opacity-8 text-center"><span class="badge bg-info">Por debajo del limite</span></p> -->
        
      </div>
    </a>
    <!-- Sensor Spects table -->
    <div v-if="showspectsprop" class="row justify-content-center mb-4">
      <div class="col-7">
        <div class="table-responsive">
          <table class="table mb-0 align-items-center">
            <tbody>
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <span class="badge bg-warning me-3">&nbsp;</span>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Limite Maximo</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <span class="text-xs font-weight-bold">{{sensorprop.max_threshold}}</span>
                  <span v-if="sensor.sensor_type=='TEMPERATURE'" class="temp_grados">&deg;</span>
                  <span v-if="sensor.sensor_type=='HUMIDITY'" class="temp_grados">%</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <span class="badge bg-info me-3">&nbsp;</span>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Limite Minimo</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <span class="text-xs font-weight-bold">{{sensorprop.min_threshold}}</span>
                  <span v-if="sensor.sensor_type=='TEMPERATURE'" class="temp_grados">&deg;</span>
                  <span v-if="sensor.sensor_type=='HUMIDITY'" class="temp_grados">%</span>  
                </td>
              </tr>
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Sensor</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <span class="text-xs font-weight-bold">{{sensorprop.unique_id}}</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Sitio</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <span class="text-xs font-weight-bold">{{ sensorSite.name }}</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Ciudad</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <span class="text-xs font-weight-bold">{{profileStore.current_organization.city}}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div v-if="showspectsprop" class="row justify-content-center mb-4">
      <div
        class="col-7"
      >
        <a href="#" @click="toggleShowHistory" class="btn w-100 bg-light">
          <i
            class="mb-1 text-sm text-secondary"
            :class="`fa fa-history`"
            aria-hidden="true"
          ></i>
         Ver Historial
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed, ref, onMounted, defineEmits, watch } from 'vue';
import useProfileStore from "@/stores/profile.js"
import useChatterBoxStore from "@/stores/chatterbox.js"

const props = defineProps(["sensorprop", "showspectsprop"]);
const emit = defineEmits(["toggleShowHistory"])

const showHistory = ref(false)

const toggleShowHistory=()=>{
  showHistory.value=!showHistory.value;
  emit("toggleShowHistory")
}

const sensor = ref({});

const isRealTimeMode = ref(false);

const chatterBoxStore = useChatterBoxStore()
let lastDataIndex = 0;
watch(chatterBoxStore.messages, (newValue) => {
  let messages = newValue;
  let sensormessages = messages[sensor.value.unique_id]
  let messagesLength = sensormessages.length
  console.log("messagesLength", messagesLength, "lastDataIndex",lastDataIndex)
  if(messagesLength-1 != lastDataIndex) {
    // console.log(messages)
    lastDataIndex = messagesLength-1
    console.log("rawdata", sensormessages[lastDataIndex])
    if(lastDataIndex > 0){
      isRealTimeMode.value=true
      let sensorNewData = sensormessages[lastDataIndex];
      sensor.value.last_value = sensorNewData.value;
      sensor.value.last_value_date = sensorNewData.date;
      sensor.value.last_value_time = sensorNewData.time;
      sensor.value.last_energy_state = sensorNewData.energy ? true:false;
    }
  }
  console.log("-------------------------")
});


// setTimeout(()=>{isRealTimeMode.value=true}, 5000)

const colorClass = computed(()=>{
  const gray = "push-indicator--gray-default"
  const green = "push-indicator--green-light"
  const blue = "push-indicator--blue-light"
  const red = "push-indicator--red-light"
  let color = gray
  if(sensor.value.last_value && !isNaN(sensor.value.last_value) && sensor.value.is_active) {
      if(sensor.value.last_value > sensor.value.max_threshold){
        color = red
      }else if(sensor.value.last_value < sensor.value.min_threshold){
        color = blue
      }else {
        color = green
      }
  }
  return color;
})

const formatedDateTime = (last_value_date, last_value_time)=>{
  let formattedDate = "aaaa-mm-dd";
  let formattedTime = "hh:mm:ss";
  if(last_value_date && last_value_time){
    // let dateObject = new Date(last_value_date);
    // formattedDate = dateObject.toISOString().split("T")[0]; // Get YYYY-MM-DD
    // formattedTime = dateObject.toISOString().split("T")[1].split(".")[0]; // Get HH:mm:ss
    formattedDate = last_value_date;
    formattedTime = last_value_time;
  }
  return `${formattedDate} | ${formattedTime}`
}

const formatedDatetime = computed(()=>{
 
  if(sensor.value.last_value_date && sensor.value.last_value_time){
    return formatedDateTime(sensor.value.last_value_date, sensor.value.last_value_time)
  }
  return ""
})

const setSensor = (data)=>{
  data.last_value = data.last_value == null ? "--.--" : data.last_value;
  sensor.value = data;
}

onMounted(()=>{
  setSensor(props.sensorprop);
});

const profileStore = useProfileStore()
const sensorSite = computed(()=>{
  if(profileStore.current_organization){
    if(profileStore.current_organization.sites){
      let site = profileStore.current_organization.sites.find((site)=>props.sensorprop.site==site.id)
      return site
    }
  }
  return ""
})
</script>

<style lang="scss" scoped>
.push-indicator {
  position: relative;
  margin: 0 auto;
  // border:1px solid red;
  border-radius: 50%;
  padding: 20px;
  width: 200px;
  height: 200px;
  // text-align: center;
}

.push-indicator--blue-light {
  background: linear-gradient(
    360deg,
    #0c9bec 0%,
    rgba(12, 155, 236, 0.42) 48.97%,
    rgba(12, 155, 236, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(6, 151, 177, 0.46);
}

.push-indicator--green-light {
  background: linear-gradient(
    360deg,
    #06b10d 0%,
    rgba(6, 145, 53, 0.42) 48.97%,
    rgba(6, 177, 13, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(6, 177, 13, 0.46);
}

.push-indicator--red-light {
  background: linear-gradient(
    360deg,
    #c91d12 0%,
    rgba(201, 29, 18, 0.42) 48.97%,
    rgba(201, 29, 18, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(201, 29, 18, 0.46);
}

.push-indicator--gray-default {
  background: linear-gradient(
    360deg,
    rgba(0,0,0,0.3) 0%,
    rgba(0,0,0,0.3) 48.97%,
    rgba(0,0,0,0.3) 100%
  );
  box-shadow: 0px 4px 4px rgba(0,0,0,0.3);
}

.push-in-indicator {
  border-radius: 50%;
  padding: 4px;
  // width: 100px;
  height: 100%;
  // margin: 0 auto;
  // border:1px solid red;
  background: #fff9f9;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.display {
  display: flex;
  border-radius: 50%;
  // border:1px solid red;
  height: 100%;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 24px;
  line-height: 33px;
  color: #a29f9f;
}

.recording-text {
  color: red;
  animation: ease pulse 2s infinite;
}

@keyframes pulse {
  0% {
    color: red;
  }
  50% {
    color: #e4e8ed;
  }
  100% {
    color: red;
  }
}
</style>
