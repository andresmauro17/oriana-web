/**
 * Global Components
 */
import AuthLayout from "@/layouts/AuthLayout.vue"
import DashboardLayout from "@/layouts/DashboardLayout.vue"
import LoginView from "@/views/Auth/LoginView.vue"
import DashboardView from "@/views/DashboardView.vue"

const GlobalComponents = {
  install(Vue) {
    Vue.component("DashboardLayout", DashboardLayout);
    Vue.component("AuthLayout", AuthLayout);
    Vue.component("LoginView", LoginView);
    Vue.component("DashboardView", DashboardView);
  },
};

export default GlobalComponents;
