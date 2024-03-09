import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import App from './App.vue'

import LoginForm from './pages/LoginForm.vue'
import RegistrationForm from './pages/RegistrationForm.vue'
import UsersList from './pages/UsersList.vue'

const app = createApp(App)

const routes = [
  { path: '/login', name: 'LoginForm', component: LoginForm },
  { path: '/registration', name: 'RegistrationForm', component: RegistrationForm },
  { path: '/users_list', name: 'UsersList', component: UsersList }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(router)

app.use(autoAnimatePlugin)

app.mount('#app')
