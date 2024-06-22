<template>
  <div>
    <AuthNavBar />
    <slot name="content"></slot>
    <AuthFooter />
  </div>
</template>

<script setup>
import AuthNavBar from "@/layouts/AuthLayout/AuthNavBar.vue";
import AuthFooter from "@/layouts/AuthLayout/AuthFooter.vue";
</script>

<style lang="scss" scoped>

</style>