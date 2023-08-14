import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import ArgonDashboard from "./argon-dashboard";

const app = createApp(App)
app.use(createPinia())
app.use(ArgonDashboard);

app.mount('#app')
