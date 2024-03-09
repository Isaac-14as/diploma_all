<script setup>
import axios from 'axios'
// import { ref } from 'vue'

// const { users } = ref([])

const getUsers = async () => {
  if (localStorage.user && JSON.parse(localStorage.user).role == 'admin') {
    try {
      const { data } = await axios.get(`https://127.0.0.1:7777/auth/all_users`, {
        withCredentials: true
      })
      console.log(data)
    } catch (err) {
      console.log(err)
    }
  } else {
    console.log('нет пользователя!')
  }
}
getUsers()
</script>

<template>
  <div class="user_get" @click="getUsers">get_users</div>
</template>

<style scoped>
.user_get {
  border: 2px solid black;
  width: 100px;
}
</style>
