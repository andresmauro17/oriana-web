import TestingComponent from "../views/testingComponent.vue";

const testingComponent = {
  install(app) {
    app.component("testing-component", TestingComponent);
  },
};

export default testingComponent;
