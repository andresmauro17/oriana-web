<template>
  <div class="wrapper">
    <!-- <notifications></notifications> -->
    <side-bar>
      <template v-slot:links>
        <a
          href="#"
          @click="showSwitchModal = true"
          class="sidebar-menu-item nav-link"
        >
          <i class="ni ni-shop text-primary"></i>
          <span class="nav-link-text"> Organizaciones </span>
          <i class="fas fa-sort text-primary text-right"></i>
        </a>
        <sidebar-item
          :link="{
            name: 'Medex Barranquilla',
            icon: 'ni ni-check-bold text-success',
            path: '/widgets',
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Sitios',
            icon: 'ni ni-ungroup text-orange',
          }"
        >
          <sidebar-item :link="{ name: 'Bodega Pricipal', path: '/pricing' }" />
          <sidebar-item :link="{ name: 'Urgencias', path: '/login' }" />
          <sidebar-item :link="{ name: 'Segundo piso', path: '/register' }" />
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Alarmas',
            icon: 'ni ni-ui-04 text-info',
            path: '/charts',
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Reportes',
            icon: 'ni ni-chart-pie-35 text-info',
            path: '/charts',
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Eventos',
            icon: 'ni ni-calendar-grid-58 text-red',
            path: '/calendar',
          }"
        >
        </sidebar-item>
      </template>
      <template v-slot:links-after>
        <hr class="my-3" />
        <h6 class="navbar-heading p-0 text-muted">Docuentacion</h6>
        <ul class="navbar-nav mb-md-3">
          <li class="nav-item">
            <a
              class="nav-link"
              href="https://demos.creative-tim.com/vue-argon-dashboard-pro/documentation"
              target="_blank"
            >
              <i class="ni ni-spaceship"></i>
              <span class="nav-link-text">Pagina de estado</span>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              href="https://demos.creative-tim.com/vue-argon-dashboard-pro/documentation/foundation/colors.html"
              target="_blank"
            >
              <i class="ni ni-palette"></i>
              <span class="nav-link-text">Manual de usuario</span>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              href="https://demos.creative-tim.com/vue-argon-dashboard-pro/documentation/components/avatars.html"
              target="_blank"
            >
              <i class="ni ni-support-16"></i>
              <span class="nav-link-text">Soporte</span>
            </a>
          </li>
        </ul>
      </template>
    </side-bar>
    <div class="main-content">
      <DashboardNavbar></DashboardNavbar>

      <div @click="$sidebar.displaySidebar(false)">
        <slot name="content"></slot>
      </div>
      <!-- <content-footer v-if="!$route.meta.hideFooter"></content-footer> -->
    </div>

    <!-- switch modal -->
    <modal :show="showSwitchModal" @update:show="showSwitchModal = $event">
      <template v-slot:header>
        <h6 class="modal-title">
          Usted tiene <strong class="text-primary">2</strong> organizaciones.
        </h6>
      </template>
      <div class="list-group list-group-flush">
        <a href="#!" class="list-group-item list-group-item-action">
          <div class="row align-items-center">
            <div class="col ml--2">
              <div class="d-flex justify-content-between align-items-center">
                <div>
                  <h4 class="mb-0 text-sm">Medex Cali</h4>
                </div>
              </div>
            </div>
          </div>
        </a>
        <a href="#!" class="list-group-item list-group-item-action">
          <div class="row align-items-center">
            <div class="col ml--2">
              <div class="d-flex justify-content-between align-items-center">
                <div>
                  <h4 class="mb-0 text-sm">
                    <i class="ni ni-check-bold text-success"></i> Medex
                    Barranquilla
                  </h4>
                </div>
                <div class="text-right">
                  <i class="ni ni-settings text-primary"></i>
                </div>
              </div>
            </div>
          </div>
        </a>
      </div>

      <template v-slot:footer>
        <base-button
          type="link"
          class="ml-auto"
          @click="showSwitchModal = false"
          >Agregar una organizacion</base-button
        >
      </template>
    </modal>
  </div>
</template>

<script setup>
// eslint-disable-next-line no-unused-vars
import DashboardNavbar from "./DashboardNavbar.vue";
// import ContentFooter from "./ContentFooter.vue";

import { onMounted, ref } from "vue";
// import { useStore } from "vuex";

// const store = useStore();
// const appSettings = computed(() => store.state.appSettings);

import PerfectScrollbar from "perfect-scrollbar";
import "perfect-scrollbar/css/perfect-scrollbar.css";

function hasElement(className) {
  return document.getElementsByClassName(className).length > 0;
}

const themeInitScrollbar = (className) => {
  if (hasElement(className)) {
    new PerfectScrollbar(`.${className}`);
  } else {
    // try to init it later in case this component is loaded async
    setTimeout(() => {
      initScrollbar(className);
    }, 100);
  }
};

// eslint-disable-next-line no-unused-vars
const showSwitchModal = ref(false);
const initScrollbar = () => {
  let isWindows = navigator.platform.startsWith("Win");
  if (isWindows) {
    themeInitScrollbar("sidenav");
  }
};

onMounted(() => {
  initScrollbar();
});
</script>
<style lang="scss">
// .dropdown-menu {
//   z-index: 10000;
// }
</style>
