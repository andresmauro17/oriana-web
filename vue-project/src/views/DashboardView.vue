<template>
  <div>
    <div class="container-fluid mt--6 min-height-600">
      <!-- breadcrumbs -->
      <div class="row align-items-center py-4">
        <div class="col-12">
            <nav aria-label="breadcrumb" class=" d-md-inline-block ml-md-4">
                <ol class="breadcrumb breadcrumb-links">
                    <li class="breadcrumb-item">
                        <a to="/"><i class="fas fa-home"></i></a>
                    </li>
                    <li class="breadcrumb-item"><a href="#">Dashboard</a></li>
                    <li class="breadcrumb-item active" aria-current="page">
                        Indicadores
                    </li>
                </ol>
            </nav>
        </div>
      </div>
      <div v-if="sensors" class="row">
        <div v-for="sensor in sensors" :key="sensor.id" class="col-xl-4 mb-4">
          <IndicatorComponent :sensorprop="sensor" :showspectsprop="false" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { defineProps, onMounted, ref } from "vue";
  import SensorService from "@/services/sensorservice.js"
  import IndicatorComponent from "@/components/Indicator/IndicatorComponent.vue";
  const props = defineProps(["site"]);

  const sensors = ref([]);
  const getDashboardSensors = ()=>{
    SensorService.getDashboardSensors().then((res)=>{
      sensors.value = res.data;
    })
  }
  onMounted(()=>{
    console.log("dashboardview",props.site)
    getDashboardSensors();
  })
</script>