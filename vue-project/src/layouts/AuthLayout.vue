<template>
  <div>
    <AuthNavbar />
    <slot name="content"></slot>
    <AuthFooter />
  </div>
</template>

<script setup>
import AuthNavbar from "@/layouts/AuthLayout/AuthNavbar.vue";
import AuthFooter from "@/layouts/AuthLayout/AuthFooter.vue";
</script>

<style lang="scss" scoped>

</style>