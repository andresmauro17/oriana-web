<template>
  <!--  border-radius-xl ms-4 my-3 -->
  <aside
    id="sidenav-main"
    class="sidenav bg-white navbar navbar-vertical navbar-expand-xs border-0  fixed-start"
    :class="` ${sidebarType}`"
  >
    <div class="sidenav-header">
      <i
        id="iconSidenav"
        class="top-0 p-3 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true"
      ></i>
      <a class="m-0 navbar-brand text-center" href="/">
        <img
          src="@/assets/img/logos/gthux/onlylogo.png"
          class="navbar-brand-img h-100"
          alt="main_logo"
        />
        G-thux
      </a>
    </div>
    <hr class="mt-0 horizontal dark" />
    <!-- <sidenav-list /> -->
    <div
      id="sidenav-collapse-main"
      class="collapse navbar-collapse w-auto h-auto h-100"
    >
      <!-- organization menu -->
      <ul class="navbar-nav" v-if="profileStore.organizations.length">
        <li class="nav-item">
          <a href="#" class="nav-link" :class="{active: showSwitchModal}" aria-controls="dashboardsExamples" role="button" aria-expanded="false" @click="showSwitchModal = true">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-building text-primary text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Organizaciones</span>
            <i class="fas fa-sort text-default text-right" style="margin-left: auto;"></i>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-check-bold text-success text-sm opacity-10"></i>
            </div>
            <span v-if="profileStore.current_organization.id" class="nav-link-text ms-1">{{profileStore.current_organization.name}}</span>
            <span v-else class="nav-link-text ms-1">Todas</span>
            <i v-if="profileStore.current_organization.id" class="fas fa-tools text-default text-right" style="margin-left: auto;"></i>
          </a>
        </li>
        <li class="nav-item">
          <a data-bs-toggle="collapse" href="#applicationsExamples" class="nav-link " aria-controls="applicationsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-ungroup text-danger text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Sitios</span>
          </a>
          <div class="collapse" :class="{show:!collapsedSites}" id="applicationsExamples">
            <ul class="nav ms-4">
              <!-- empty site -->
              <li class="nav-item ">
                <a class="nav-link " :href="`/sites/0/switch/`">
                  <div v-if="!profileStore.currentuser.current_site" class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
                    <i class="ni ni-check-bold text-success text-sm opacity-10"></i>
                  </div>
                  <span class="sidenav-mini-icon"> Todos  </span>
                  <span class="sidenav-normal"> Todos </span>
                </a>
              </li>
              <!-- iterating sites -->
              <li class="nav-item " v-for="site in profileStore.current_organization.sites" :key="site.id">
                <a class="nav-link " :href="`/sites/${site.id}/switch/`">
                  <div v-if="site.id==profileStore.currentuser.current_site" class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
                    <i class="ni ni-check-bold text-success text-sm opacity-10"></i>
                  </div>
                  <span class="sidenav-mini-icon"> {{site.name}} </span>
                  <span class="sidenav-normal"> {{site.name}}</span>
                </a>
              </li>
            </ul>
          </div>
        </li>
        <hr class="mt-0 horizontal dark" />
      </ul>
      <!-- main menu -->
      <ul class="navbar-nav">
        <li class="nav-item">
          <a href="/" :class="isActiveIfIsRoot()" class="nav-link " aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-shop text-primary text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Dashboard</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="/status" :class="isActive([`/status/`])" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-bullet-list-67 text-primary text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Status</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link " aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-ui-04 text-info text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Alarmas</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-chart-pie-35 text-info text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Reportes</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-calendar-grid-58 text-danger text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Eventos</span>
          </a>
        </li>
      </ul>
      <!-- docs menu -->
      <ul class="navbar-nav">
        <li class="mt-3 nav-item">
          <hr class="mt-0 horizontal dark" />
          <h6
            class="text-xs ps-4 ms-2 text-uppercase font-weight-bolder opacity-6"
            :class="'ms-2'"
          >
            Docs
          </h6>
        </li>
        <li class="nav-item">
          <a href="https://stats.uptimerobot.com/ZxQm5CPDX8" target="blank" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-spaceship text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Pagina de estado</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="https://tidal-consonant-eec.notion.site/Centro-de-ayuda-sistema-de-monitoreo-continuo-G-THUX-08010899dca54e64b1856e5931f96ea5?pvs=4" target="blank" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-palette text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Manual de usuario</span>
          </a>
        </li>
        <li class="nav-item">
          
            <!-- <a href="https://ingenialo.atlassian.net/servicedesk/customer/portals" target="blank" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false"> -->
            <a href="https://wa.me/573173099005" target="blank" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-support-16 text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Soporte</span>
          </a>
        </li>
      </ul>
    </div>
    <!-- switch modal -->
    <teleport to='body'>
      <!-- switch modal -->
      <Modal :show="showSwitchModal" @update:show="showSwitchModal = $event">
        <template v-slot:header>
          <h6 class="modal-title">
            Usted tiene <strong class="text-primary"> {{profileStore.organizations.length}} </strong> Organizaciones:
          </h6>
        </template>
        <div class="list-group list-group-flush" v-if="profileStore.organizations">
          <!-- Todas -->
          <a :href="`/organizations/0/switch/`" class="list-group-item list-group-item-action">
            <div class="row align-items-center">
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">
                      <i class="ni ni-check-bold text-success" v-if="!profileStore.current_organization.id"></i>
                      Todas
                    </h4>
                  </div>
                </div>
              </div>
            </div>
          </a>
          <!-- iterating orgs -->
          <a :href="`/organizations/${organization.id}/switch/`" class="list-group-item list-group-item-action" v-for="organization in profileStore.organizations" :key="organization.id" >
            <div class="row align-items-center">
              <div class="col ml--2">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h4 class="mb-0 text-sm">
                      <i class="ni ni-check-bold text-success" v-if="organization.id == profileStore.currentuser.current_organization"></i>
                      {{organization.name}}
                    </h4>
                  </div>
                  <div class="text-right" v-if="organization.id == profileStore.currentuser.current_organization">
                    <i class="ni ni-settings text-primary"></i>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
        <template v-slot:footer>
          <!-- <a class="mb-0 btn btn-link pe-3 ps-0 ms-auto" href="#">
            Agregar una organizacion
          </a> -->
        </template>
      </Modal>
    </teleport>
  </aside>
  
</template>

<script setup>
import { ref } from "vue";
import Modal from "@/components/Modals/Modal.vue"
import useProfileStore from "@/stores/profile.js"

const showSwitchModal = ref(false);

const collapsedSites = ref(false);// thisis the default behivor forsites menu

const sidebarType=ref("bg-white");//bg-white bg-default;

const profileStore = useProfileStore()

function isActive(paths) {
  return paths.includes(window.location.pathname) ? "active" : "";
}
function isActiveIfIsRoot() {
  return window.location.pathname === "/"?"active" : "";
}
</script>

<style lang="scss" scoped>

</style>