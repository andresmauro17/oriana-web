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
      <IndicatorComponent :sensorprop="sensorData" :showspectsprop="true" />
    </div>
    <!-- <div class="card shadow-lg mx-4">
      <div class="card-body p-3">
        <div class="row gx-4">
          <IndicatorComponent :sensorprop="sensorData" />
        </div>
      </div>
    </div> -->


  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue';
  import useProfileStore from "@/stores/profile.js"
  import IndicatorComponent from "@/components/Indicator/IndicatorComponent.vue";
  
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