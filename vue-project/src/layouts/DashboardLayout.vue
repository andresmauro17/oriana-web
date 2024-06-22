<template>
  <div>
    <div class="min-height-300 position-absolute w-100"></div>
    <SidebarComponent />
    <main class="main-content position-relative max-height-vh-100 h-100">
      <NavbarComoponent />
      <slot name="content"></slot>
      <FooterComponent />
    </main>
  </div>
</template>

<script setup>
import SidebarComponent from './DashboardLayout/SidebarComponent.vue';
import NavbarComoponent from './DashboardLayout/NavbarComoponent.vue';
import FooterComponent from './DashboardLayout/FooterComponent.vue';
</script>
