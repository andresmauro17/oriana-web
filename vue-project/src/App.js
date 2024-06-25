import { onMounted } from "vue";
import useProfileStore from "@/stores/profile.js";

const App = {
  setup() {
    const profileStore = useProfileStore();
    const init = () => {
      profileStore.getCurrentUser();
      profileStore.getOrganizations();
    };
    onMounted(() => {
      console.log("heyyyy 😎")
      init();
    });
    return {
    };
  },
};
export default App;