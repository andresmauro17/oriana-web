import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.js'
import GlobalComponents from "./globalComponents";

import ArgonDashboard from "./argon-dashboard";

const app = createApp(App)
app.use(createPinia())
app.use(ArgonDashboard);
app.use(GlobalComponents);

app.mount('#app')
