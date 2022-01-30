import DashboardLayout from "../views/Layout/DashboardLayout.vue";
import AuthLayout from "../views/Layout/AuthLayout.vue";
import TestingComponent from "../views/testingComponent.vue";
import Dashboard from "../views/Dashboard/dashboard.vue";
import Login from "../views/Auth/Login.vue";

const testingComponent = {
  install(app) {
    app.component("dashboard-layout", DashboardLayout);
    app.component("auth-layout", AuthLayout);
    app.component("testing-component", TestingComponent);
    app.component("dashboard", Dashboard);
    app.component("login", Login);
  },
};

export default testingComponent;
