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
    <ul class="navbar-nav">
        <li class="nav-item">
          <a href="#" class="nav-link active" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-shop text-primary text-sm opacity-10"></i>
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
            <span class="nav-link-text ms-1">Medex Cali</span>
            <i class="fas fa-tools text-default text-right" style="margin-left: auto;"></i>
          </a>
        </li>
        <hr class="mt-0 horizontal dark" />
        <li class="nav-item">
          <a data-bs-toggle="collapse" href="#applicationsExamples" class="nav-link " aria-controls="applicationsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-ungroup text-danger text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Sitios</span>
          </a>
          <div class="collapse " id="applicationsExamples">
            <ul class="nav ms-4">
              <li class="nav-item ">
                <a class="nav-link " href="#">
                  <span class="sidenav-mini-icon"> B </span>
                  <span class="sidenav-normal"> Bodega Principal </span>
                </a>
              </li>
              <li class="nav-item ">
                <a class="nav-link " href="#">
                  <span class="sidenav-mini-icon"> U </span>
                  <span class="sidenav-normal"> Urgencias </span>
                </a>
              </li>
            </ul>
          </div>
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
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-spaceship text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Pagina de estado</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-palette text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Manual de usuario</span>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link" aria-controls="dashboardsExamples" role="button" aria-expanded="false">
            <div class="icon icon-shape icon-sm text-center d-flex align-items-center justify-content-center">
              <i class="ni ni-support-16 text-dark text-sm opacity-10"></i>
            </div>
            <span class="nav-link-text ms-1">Soporte</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script setup>
import { ref } from "vue";

const sidebarType=ref("bg-white");//bg-white bg-default;

</script>

<style lang="scss" scoped>

</style>