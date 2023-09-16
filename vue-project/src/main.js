// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import "bootstrap/dist/js/bootstrap.min.js";
import App from './App.js'
import GlobalComponents from "./globalComponents";

import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";

import ArgonDashboard from "./argon-dashboard";

const app = createApp(App)
app.use(createPinia())
app.use(ArgonDashboard);
app.use(GlobalComponents);

app.mount('#app')
