<template>
  <nav class="navbar navbar-main navbar-expand-lg px-0 me-4 shadow-none border-radius-xl z-index-sticky border-bottom" id="navbarBlur" data-scroll="false">
    <div class="container-fluid py-1 px-3">
      <!-- Hamburguer desktop -->
      <div class="sidenav-toggler sidenav-toggler-inner d-xl-block d-none">
        <a href="#" class="p-0 nav-link text-body" @click.prevent="navbarMinimize">
          <div class="sidenav-toggler-inner">
            <i class="sidenav-toggler-line opacity-8 bg-dark"></i>
            <i class="sidenav-toggler-line opacity-8 bg-dark"></i>
            <i class="sidenav-toggler-line opacity-8 bg-dark"></i>
          </div>
        </a>
      </div>

      <div class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4" id="navbar">
        <div class="ms-md-auto pe-md-3 d-flex align-items-center"></div>
        <ul class="navbar-nav  justify-content-end">
          <!-- Notifications -->
          <li class="nav-item dropdown ps-3 d-flex align-items-center">
            <a href="javascript:;" class="nav-link text-dark p-0" id="dropdownNotifications" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="fa fa-bell cursor-pointer"></i>
            </a>
            <ul class="dropdown-menu dropdown-menu-end px-2 py-3 me-sm-n4" aria-labelledby="dropdownNotifications">
              <li class="mb-2">
                <!-- <a class="dropdown-item border-radius-md" href="javascript:;">
                  <div class="d-flex py-1">
                    <div class="my-auto">
                      <img src="../../assets/img/team-2.jpg" class="avatar avatar-sm  me-3 " alt="user image">
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="text-sm font-weight-normal mb-1">
                        <span class="font-weight-bold">New message</span> from Laur
                      </h6>
                      <p class="text-xs text-secondary mb-0">
                        <i class="fa fa-clock me-1"></i>
                        13 minutes ago
                      </p>
                    </div>
                  </div>
                </a> -->
              </li>
            </ul>
          </li>

          <!-- avatar -->
          <li class="nav-item dropdown ps-3 d-flex align-items-center">
            <ArgonAvatar img="https://demos.creative-tim.com/vue-soft-ui-dashboard-pro/img/team-1.66f62826.jpg" alt="Avatar" size="sm" circular href="javascript:;" id="dropdownAvatar" data-bs-toggle="dropdown" aria-expanded="false" />
            <ul class="dropdown-menu dropdown-menu-end px-2 py-3 me-sm-n4" aria-labelledby="dropdownAvatar">
              <li class="mb-2">
                <h6 class=" dropdown-item text-overflow m-0">Andres Cuervo</h6>
              </li>
              <li class="mb-2">
                <a href="#!" class="dropdown-item">
                  <i class="ni ni-single-02"></i>
                  <span class="ms-1">Mi perfil</span>
                </a>
              </li>
              <li class="mb-2">
                <a href="#!" class="dropdown-item">
                  <i class="ni ni-settings-gear-65"></i>
                  <span class="ms-1">Configuracion</span>
                </a>
              </li>
              <div class="dropdown-divider"></div>
              <li class="mb-2">
                <a href="/logout" class="dropdown-item">
                  <i class="ni ni-user-run"></i>
                  <span class="ms-1">Salir</span>
                </a>
              </li>
            </ul>
          </li>

           <!-- Hamburguer mobile -->
           <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
            <a href="javascript:;" class="nav-link text-white p-0" id="iconNavbarSidenav" @click.prevent="navbarMinimize">
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line bg-dark"></i>
                <i class="sidenav-toggler-line bg-dark"></i>
                <i class="sidenav-toggler-line bg-dark"></i>
              </div>
            </a>
          </li>

        </ul>
      </div>

    </div>
  </nav>
</template>

<script setup>
import ArgonAvatar from "@/components/ArgonAvatar.vue"
const navbarMinimize = ()=>{
  const sidenav_show = document.querySelector("#app");

  if (sidenav_show.classList.contains("g-sidenav-show") && sidenav_show.classList.contains("g-sidenav-hidden")) {
    sidenav_show.classList.add("g-sidenav-pinned");
    sidenav_show.classList.remove("g-sidenav-hidden");
  } else if (sidenav_show.classList.contains("g-sidenav-show") && sidenav_show.classList.contains("g-sidenav-pinned")) {
    sidenav_show.classList.add("g-sidenav-hidden");
    sidenav_show.classList.remove("g-sidenav-pinned");
  } else if (sidenav_show.classList.contains("g-sidenav-show") && window.innerWidth < 1200 ) {
    sidenav_show.classList.add("g-sidenav-pinned");
  } else {
    sidenav_show.classList.add("g-sidenav-hidden");
  }
}
</script>

<style lang="scss" scoped>

</style>