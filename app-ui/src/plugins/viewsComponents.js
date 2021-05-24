import DashboardLayout from "../views/Layout/DashboardLayout.vue";
import TestingComponent from "../views/testingComponent.vue";
import Dashboard from "../views/Dashboard/dashboard.vue";

const testingComponent = {
  install(app) {
    app.component("dashboard-layout", DashboardLayout);
    app.component("testing-component", TestingComponent);
    app.component("dashboard", Dashboard);
  },
};

export default testingComponent;
