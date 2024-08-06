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
          <a :href="`/admin/${sensor.legacy?'app_amarey/nevera':'app_sensors/sensor'}/${sensor.id}/change/`" target="blank" class="mb-0 btn btn-xs bg-neutral">
            <i class="fas fa-cog "></i> 
            Config
          </a>
        </div>
    </div>
    <!-- Card body -->
    <a :href="`/${sensor.legacy?'sensorslegacy':'sensors'}/${sensor.id}`">
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
              <tr v-if="sensorSite">
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
              <!-- <tr>
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
              </tr> -->
              <tr>
                <td>
                  <div class="px-2 py-0 d-flex">
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">Calibraciones</h6>
                    </div>
                  </div>
                </td>
                <td class="text-sm text-center align-middle">
                  <a href="#" @click="()=>openCertsModal=true">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf" viewBox="0 0 16 16">
                      <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1"/>
                      <path d="M4.603 12.087a.8.8 0 0 1-.438-.42c-.195-.388-.13-.776.08-1.102.198-.307.526-.568.897-.787a7.7 7.7 0 0 1 1.482-.645 20 20 0 0 0 1.062-2.227 7.3 7.3 0 0 1-.43-1.295c-.086-.4-.119-.796-.046-1.136.075-.354.274-.672.65-.823.192-.077.4-.12.602-.077a.7.7 0 0 1 .477.365c.088.164.12.356.127.538.007.187-.012.395-.047.614-.084.51-.27 1.134-.52 1.794a11 11 0 0 0 .98 1.686 5.8 5.8 0 0 1 1.334.05c.364.065.734.195.96.465.12.144.193.32.2.518.007.192-.047.382-.138.563a1.04 1.04 0 0 1-.354.416.86.86 0 0 1-.51.138c-.331-.014-.654-.196-.933-.417a5.7 5.7 0 0 1-.911-.95 11.6 11.6 0 0 0-1.997.406 11.3 11.3 0 0 1-1.021 1.51c-.29.35-.608.655-.926.787a.8.8 0 0 1-.58.029m1.379-1.901q-.25.115-.459.238c-.328.194-.541.383-.647.547-.094.145-.096.25-.04.361q.016.032.026.044l.035-.012c.137-.056.355-.235.635-.572a8 8 0 0 0 .45-.606m1.64-1.33a13 13 0 0 1 1.01-.193 12 12 0 0 1-.51-.858 21 21 0 0 1-.5 1.05zm2.446.45q.226.244.435.41c.24.19.407.253.498.256a.1.1 0 0 0 .07-.015.3.3 0 0 0 .094-.125.44.44 0 0 0 .059-.2.1.1 0 0 0-.026-.063c-.052-.062-.2-.152-.518-.209a4 4 0 0 0-.612-.053zM8.078 5.8a7 7 0 0 0 .2-.828q.046-.282.038-.465a.6.6 0 0 0-.032-.198.5.5 0 0 0-.145.04c-.087.035-.158.106-.196.283-.04.192-.03.469.046.822q.036.167.09.346z"/>
                    </svg>
                    ver documentos
                  </a>
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
    <div class="card-footer" v-if="delayedHours>hourTreshold">
      <ArgonBadge color="danger" size="lg" class="w-100"> No trasmite hace {{delayedHours}} horas!</ArgonBadge>
    </div>
    <teleport to='body'>
      <CertificatesModal :sensor="sensorprop" :showmodal="openCertsModal" @upDateShowModal="(event)=>openCertsModal=event"/>
    </teleport>
  </div>
</template>

<script setup>
import { defineProps, computed, ref, onMounted, defineEmits, watch } from 'vue';
import ArgonBadge from "@/components/ArgonBadge.vue";
import CertificatesModal from "@/components/Modals/CertificatesModal.vue";
import useProfileStore from "@/stores/profile.js"
import useChatterBoxStore from "@/stores/chatterbox.js"

const props = defineProps(["sensorprop", "showspectsprop"]);
const emit = defineEmits(["toggleShowHistory"])
const openCertsModal = ref(false);
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

const formatDateTime = (last_value_date, last_value_time)=>{
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
    return formatDateTime(sensor.value.last_value_date, sensor.value.last_value_time)
  }
  return ""
})

const hourTreshold = 2;
const delayedHours = ref(0);
const setSensor = (data)=>{

  //calculate delayed hours
  const lastValueDateTime = new Date(`${data.last_value_date}T${data.last_value_time}`);
  const now = new Date();
  const differenceInMilliseconds = now - lastValueDateTime;
  delayedHours.value = Math.floor(differenceInMilliseconds / (1000 * 60 * 60));

  data.last_value = data.last_value == null ? "--.--" : data.last_value;
  sensor.value = data;
}

onMounted(()=>{
  setSensor(props.sensorprop);
});

const profileStore = useProfileStore()
const sensorSite = computed(()=>{
  let site = null;
  if(props.sensorprop.legacy){
    site =  profileStore.sites.find((site)=>props.sensorprop.site==site.empresa_id_amarey)
  }else{
    site =  profileStore.sites.find((site)=>props.sensorprop.site==site.id)
  }
  return site
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
