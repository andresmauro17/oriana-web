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
                  <li class="breadcrumb-item"><a :href="`/sites/${sensorSite.id}/switch/`">{{ sensorSite.name }}</a></li>
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
  const showHistory = ref(true);
  const profileStore = useProfileStore()
  const sensorSite = computed(()=>{
    if(profileStore.current_organization){
      if(profileStore.current_organization.sites){
        let site = profileStore.current_organization.sites.find((site)=>sensorData.value.site==site.id)
        return site
      }
    }
   return ""
  })
  profileStore.current_organization.sites
  
  const sensorData = ref({});
  sensorData.value = JSON.parse(document.getElementById('sensor_serialized').textContent);
  onMounted(() => {
    console.log("hola", sensorData.value);
  })
</script>

<style lang="scss" scoped>

</style>