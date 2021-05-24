/*!

=========================================================
* Vue Argon Dashboard PRO - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

* Coded by www.creative-tim.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

import { createApp } from "vue";
import { createStore } from "vuex";
import App from "./App.js";
import ArgonDashboard from "./plugins/argon-dashboard";
import "element-plus/lib/theme-chalk/index.css";

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import storejs from "./store";

const options = { containerClassName: "ct-notification" };

const store = createStore(storejs);

const appInstance = createApp(App);
appInstance.use(store);
appInstance.use(Toast, options);
appInstance.use(ArgonDashboard);
appInstance.mount("#app");
