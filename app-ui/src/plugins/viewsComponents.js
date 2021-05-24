import TestingComponent from "../views/testingComponent.vue";
import DashboardLayout from "../views/Layout/DashboardLayout.vue";

const testingComponent = {
  install(app) {
    app.component("testing-component", TestingComponent);
    app.component("dashboard-layout", DashboardLayout);
  },
};

export default testingComponent;
