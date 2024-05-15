import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import App from './App.vue'

import LoginForm from './pages/LoginForm.vue'
// import RegistrationForm from './components/RegistrationForm.vue'
// import UsersList from './components/UsersList.vue'

import ManagementLog from './pages/ManagementLog.vue'
import AccidentLog from './pages/AccidentLog.vue'
import UserAdmin from './pages/UserAdmin.vue'
import Graph from './pages/Graph.vue'
import Mnemo from './pages/Mnemo.vue'

import panZoom from 'vue-panzoom'
import Devices from './pages/Devices.vue'
import DeviceValue from './pages/DeviceValue.vue'

const app = createApp(App)

app.use(panZoom)
const routes = [
  { path: '/', name: 'LoginForm', component: LoginForm },
  { path: '/device_value/:id', name: 'DeviceValue', component: DeviceValue },
  { path: '/graph', name: 'Graph', component: Graph },
  { path: '/management_log', name: 'ManagementLog', component: ManagementLog },
  { path: '/accident_log', name: 'AccidentLog', component: AccidentLog },
  { path: '/user_admin', name: 'UserAdmin', component: UserAdmin },
  { path: '/mnemo', name: 'Mnemo', component: Mnemo },
  { path: '/devices', name: 'Devices', component: Devices }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(router)

app.use(autoAnimatePlugin)

app.mount('#app')
