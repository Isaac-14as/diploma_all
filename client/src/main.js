import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import App from './App.vue'

import LoginForm from './pages/LoginForm.vue'
// import RegistrationForm from './components/RegistrationForm.vue'
// import UsersList from './components/UsersList.vue'

import UserAdmin from './pages/UserAdmin.vue'
import Mnemo from './pages/Mnemo.vue'

import panZoom from 'vue-panzoom'
import Devices from './pages/Devices.vue'

const app = createApp(App)

// const app = createApp({
//   render: () => h(App)
// })
app.use(panZoom)
const routes = [
  { path: '/', name: 'LoginForm', component: LoginForm },
  // { path: '/registration', name: 'RegistrationForm', component: RegistrationForm },
  // { path: '/users_list', name: 'UsersList', component: UsersList },
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
