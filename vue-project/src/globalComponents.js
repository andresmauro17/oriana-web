/**
 * Global Components
 */
import AuthLayout from "@/layouts/AuthLayout.vue"
import MainLayout from "@/layouts/MainLayout.vue"
import LoginView from "@/views/Auth/LoginView.vue"

const GlobalComponents = {
  install(Vue) {
    Vue.component("MainLayout", MainLayout);
    Vue.component("AuthLayout", AuthLayout);
    Vue.component("LoginView", LoginView);
  },
};

export default GlobalComponents;
