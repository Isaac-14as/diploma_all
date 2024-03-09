<script setup>
import { ref } from 'vue'

import axios from 'axios'

const userName = ref('')
// watch(localStorage.getItem('user'), () => {
//   userName.value = 'Dmitriy'
// })

// console.log(localStorage.getItem('user'))
// localStorage.clear()
// localStorage.user = '123'
if (localStorage.user) {
  console.log('есть пользователь!')
  userName.value = JSON.parse(localStorage.user).name
} else {
  console.log('нет пользователя!')
}

const exitUser = async () => {
  try {
    const { data } = await axios.post(
      `https://127.0.0.1:7777/auth/logout`,
      // дает возможность устанавливать cookies
      { withCredentials: true }
    )
    localStorage.removeItem('user')
    // обновление страницы
    location.reload()
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
      <div class="name">{{ userName }}</div>
      <div class="symbol">|</div>
      <div class="exit" @click="exitUser"><b>Выйти</b></div>
    </div>
    <div></div>
  </header>
</template>

<style scoped>
header {
  background: #009485;
  height: 100px;
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
