<template>
  <div>
    <!-- hola dashboardlayout -->
    <div class="min-height-300 bg-primary position-absolute w-100">
      
    </div>
    <SidebarComponent />
    <slot name="content"></slot>
  </div>
</template>

<script setup>
import SidebarComponent from './DashboardLayout/SidebarComponent.vue';
</script>
