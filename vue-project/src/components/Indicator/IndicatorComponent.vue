<template>
  <div class="card">
    <!-- Card header -->
    <div class="card-header py-3 d-flex align-items-center border-bottom">
        <div class="d-flex align-items-center">
          <!-- Surtitle -->
          <!-- <h6 class="surtitle">5/23 projects</h6> -->
          <!-- Title -->
          <h5 class="text-capitalize">{{ sensor.name }}</h5>
        </div>
        <div class="text-end ms-auto">
          <a :href="`/sensor/${sensor.id}`" class="mb-0 btn btn-xs bg-neutral">
            <i class="fas fa-cog "></i> 
            Config
          </a>
        </div>
    </div>
    <!-- Card body -->
    <div class="card-body card-body-indicator">
      <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab dolorum natus architecto aliquam, labore accusamus error ut dolorem nobis quo odio? Tenetur pariatur ad perspiciatis culpa, mollitia ipsa placeat iusto?</p> -->
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
      <p class="mt-3 mb-0 text-center" >{{formatedDatetime}}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed, ref, onMounted } from 'vue';
const props = defineProps(["sensorprop"]);


const sensor = ref({});

const colorClass = computed(()=>{
  const gray = "push-indicator--gray-default"
  const green = "push-indicator--green-light"
  const blue = "push-indicator--blue-light"
  const red = "push-indicator--red-light"
  let color = gray
  if(sensor.value.last_value && !isNaN(sensor.value.last_value)) {
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

const formatedDatetime = computed(()=>{
  let formattedDate = "aaaa-mm-dd";
  let formattedTime = "hh:mm:ss";
  if(sensor.value.last_value_date_time){
    let dateObject = new Date(sensor.value.last_value_date_time);
    formattedDate = dateObject.toISOString().split("T")[0]; // Get YYYY-MM-DD
    formattedTime = dateObject.toISOString().split("T")[1].split(".")[0]; // Get HH:mm:ss
  }
  return `${formattedDate} | ${formattedTime}`
})

const setSensor = (data)=>{
  data.last_value = data.last_value == null ? "--.--" : data.last_value;
  sensor.value = data;
}

onMounted(()=>{
  setSensor(props.sensorprop);
});

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
</style>
