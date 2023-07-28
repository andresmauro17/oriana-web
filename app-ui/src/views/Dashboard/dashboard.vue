<template>
  <div>
    <base-header class="pb-6" type="">
      <div class="row align-items-center py-4">
        <div class="col-lg-6 col-7">
          <h6 class="h2 d-inline-block mb-0">Gthux</h6>
          <nav aria-label="breadcrumb" class="d-none d-md-inline-block ml-md-4">
            <ol class="breadcrumb breadcrumb-links">
              <li class="breadcrumb-item">
                <!-- <router-link to="/"><i class="fas fa-home"></i></router-link> -->
              </li>
              <li class="breadcrumb-item"><a href="#">Dashboard</a></li>
              <li class="breadcrumb-item active" aria-current="page">
                Indicadores
              </li>
            </ol>
          </nav>
        </div>
        <div class="col-lg-6 col-5 text-right">
          <base-button size="sm" type="neutral">New</base-button>
          <base-button size="sm" type="neutral">Filters</base-button>
        </div>
      </div>
    </base-header>
    <div class="container-fluid mt--6">
      <div class="row">
        <div class="col-xl-4">
          <indicator />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Indicator from "@/components/indicator/Indicator.vue";
export default {
  mounted() {
    console.log("dashboard mounted");
  },
  components: {
    Indicator,
  },
};
</script>

<style></style>
