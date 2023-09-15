<template>
  <div>
    <div class="container-fluid mt--6">
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
      <div class="row">
        <div class="col-xl-4">
          <IndicatorComponent />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import IndicatorComponent from "@/components/Indicator/IndicatorComponent.vue";
</script>