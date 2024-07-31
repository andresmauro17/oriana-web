import { onMounted } from "vue";
import useProfileStore from "@/stores/profile.js";

const App = {
  setup() {
    const profileStore = useProfileStore();
    const init = async () => {
      await profileStore.getCurrentUser();
      await profileStore.getOrganizations();
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
