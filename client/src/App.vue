<script setup>
import { ref, provide } from 'vue'

import Header from './components/Header.vue'

const current_user = ref('')
const access_token = ref('')

if (localStorage.user && localStorage.access_token) {
  current_user.value = JSON.parse(localStorage.user)
  access_token.value = localStorage.access_token
}
provide('current_user', current_user)
provide('access_token', access_token)

// import panZoom from 'vue-panzoom'
</script>

<template>
  <Header />
  <router-view> </router-view>
</template>

<style scoped>
.zoom_box {
  width: 300px;
  height: 300px;
  border: 1px solid black;
  overflow: hidden;
}
</style>
