<script setup>
import { inject } from 'vue'
import axios from 'axios'

// import { useRouter } from 'vue-router'

// const router = useRouter()

var API_port = import.meta.env.VITE_API_ENDPOINT

const sidebar_flag = inject('sidebar_flag')

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

const sidebarChange = () => {
  sidebar_flag.value = !sidebar_flag.value
}
</script>

<template>
  <header>
    <!-- <img class="logo" src="/src/components/logo.png" /> -->
    <div class="left_nav_menu">
      <img src="/icons8-menu.svg" alt="" class="sidebar" @click="sidebarChange" />
      <router-link to="/mnemo" class="left_link">Мнемосхема</router-link>
      <router-link v-if="current_user.role === 'admin'" to="/user_admin" class="left_link"
        >Управление пользователями</router-link
      >
    </div>

    <!-- <div class="nav_menu">234234</div> -->
    <div class="user_name">
      <div class="name">{{ current_user.name }}</div>
      <div class="symbol">|</div>
      <router-link to="/" class="exit" @click="logoutUser"><b>Выйти</b></router-link>
      <!-- <router-link v-else to="/login" class="exit">Войти</router-link> -->
    </div>
  </header>
</template>

<style scoped>
header {
  background: #009485;
  height: 80px;
  /* width: 100%; */
  display: flex;
  justify-content: space-between;
  /* justify-content: space-around; */
  align-items: center;
  font-size: 20px;
}

.left_nav_menu {
  margin-left: 20px;
  display: flex;
  align-items: center;
  font-size: 23px;
}
.left_link {
  margin-left: 40px;
}

.sidebar {
  cursor: pointer;
}

.left_link:hover {
  color: aliceblue;
  transition: 0.2s;
}

.user_name {
  display: flex;
  gap: 10px;
  margin-right: 40px;
  /* justify-content: flex-end; */
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
