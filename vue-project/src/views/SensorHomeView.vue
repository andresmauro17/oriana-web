<template>
  <div class="container-fluid mt-4 min-height-600">
    <!-- breadcrumbs -->
    <div class="row align-items-center py-4">
      <div class="col-12">
          <nav aria-label="breadcrumb" class=" d-md-inline-block ml-md-4">
              <ol class="breadcrumb breadcrumb-links">
                  <li class="breadcrumb-item">
                      <a href="/"><i class="fas fa-home"></i></a>
                  </li>
                  <li class="breadcrumb-item" v-if="sensorSite"><a :href="`/sites/${sensorSite.id}/switch/`">{{ sensorSite.name }}</a></li>
                  <li class="breadcrumb-item active" aria-current="page">
                    {{sensorData.name}}
                  </li>
              </ol>
          </nav>
      </div>
    </div>
    <div class="row gx-4">
      <IndicatorComponent :sensorprop="sensorData" :showspectsprop="true" @toggleShowHistory="()=>{showHistory= !showHistory}" />
    </div>
    <div v-if="showHistory" class="row gx-4 mt-4">
      <SensorHistoryComponent :sensorData="sensorData" />
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue';
  import useProfileStore from "@/stores/profile.js"
  import IndicatorComponent from "@/components/Indicator/IndicatorComponent.vue";
  import SensorHistoryComponent from "./SensorHomeView/SensorHistoryComponent.vue"
  import useChatterBoxStore from "@/stores/chatterbox.js"

  const showHistory = ref(true);
  const profileStore = useProfileStore()
  const sensorSite = computed(()=>{
    let site = null;
    if(sensorData.value.legacy){
      site =  profileStore.sites.find((site)=>sensorData.value.site==site.empresa_id_amarey)
    }else{
      site =  profileStore.sites.find((site)=>sensorData.value.site==site.id)
    }
   return site
  })
  
  const sensorData = ref({});
  sensorData.value = JSON.parse(document.getElementById('sensor_serialized').textContent);

  const chatterBoxStore = useChatterBoxStore()
  onMounted(() => {
    chatterBoxStore.startMqttClient(sensorData.value.unique_id)
    setTimeout(()=>{
      chatterBoxStore.startMqttClient("ffffffff")
    }, 5000)
  })
</script>

<style lang="scss" scoped>

</style>