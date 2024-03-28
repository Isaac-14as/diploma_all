<script setup>
import { inject } from 'vue'

import axios from 'axios'

var API_port = import.meta.env.VITE_API_ENDPOINT

const current_user = inject('current_user')
const access_token = inject('access_token')

const logoutUser = async () => {
  try {
    const { data } = await axios.post(`http://` + API_port + `/auth/logout`)
    current_user.value = ''
    access_token.value = ''
    localStorage.removeItem('user')
    localStorage.removeItem('access_token')
    return data
  } catch (err) {
    console.log(err)
  }
}
</script>

<template>
  <header>
    <router-link to="/users_list">Users</router-link>
    <div class="logo">123</div>
    <div class="nav_menu">234234</div>
    <div class="user_name">
      <div class="name">{{ current_user.name }}</div>
      <div class="symbol" v-if="current_user">|</div>
      <div v-if="current_user" class="exit" @click="logoutUser"><b>Выйти</b></div>
      <router-link v-else to="/login" class="exit">Войти</router-link>
    </div>
    <div></div>
  </header>
</template>

<style scoped>
header {
  background: #009485;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 20px;
}

.logo {
  /* background: #40e742; */
  width: 100px;
}

.nav_menu {
  /* background: #4064e7; */
  width: 1000px;
}

.user_name {
  /* background: #d74444; */
  width: 400px;
  display: flex;
  gap: 10px;
  align-content: center;
  justify-content: flex-end;
}

.exit {
  transition: 0.2s;
  cursor: pointer;
}

.exit:hover {
  color: aliceblue;
  transition: 0.2s;
}
</style>
