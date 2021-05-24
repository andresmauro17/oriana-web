import { mapState } from "vuex";

const App = {
  el: "#app",
  computed: {
    ...mapState(["appSettings"]),
  },
  methods: {
    getAppSettings() {
      this.$store.commit("setAppSettings", {});
    },
  },
};

export default App;
