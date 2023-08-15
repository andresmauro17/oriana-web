/**
 * Global Components
 */
import MainLayout from "@/layouts/MainLayout.vue"

const GlobalComponents = {
  install(Vue) {
    Vue.component("MainLayout", MainLayout);
  },
};

export default GlobalComponents;
