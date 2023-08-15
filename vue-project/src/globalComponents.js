/**
 * Global Components
 */
import MainLayout from "@/layouts/MainLayout.vue"
import LoginView from "@/views/Auth/LoginView.vue"

const GlobalComponents = {
  install(Vue) {
    Vue.component("MainLayout", MainLayout);
    Vue.component("LoginView", LoginView);
  },
};

export default GlobalComponents;
