<script setup>
import { reactive, provide, inject, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

import MnemonicDiagram from '@/components/MnemonicDiagram.vue'

const access_token = inject('access_token')
var API_port = import.meta.env.VITE_API_ENDPOINT

const readings = reactive([
  { s: 1, p: 1, q: 1, u: 1, i: 1, cos: 1 },
  { s: 2, p: 2, q: 2, u: 2, i: 2, cos: 2 },
  { s: 3, p: 3, q: 3, u: 3, i: 3, cos: 3 },
  { s: 4, p: 4, q: 4, u: 4, i: 4, cos: 4 }
])

const getLastValue = async (id) => {
  try {
    const { data } = await axios.get(
      `http://` + API_port + `/device/get_last_value_device_by_id/${id}`,
      {
        headers: { Authorization: access_token.value }
      }
    )
    readings[id - 1].s = data.full_power
    readings[id - 1].p = data.active_power
    readings[id - 1].q = data.reactive_power
    readings[id - 1].u = data.voltage
    readings[id - 1].i = data.amperage
    readings[id - 1].cos = data.power_factor
    return data
  } catch (err) {
    console.log(err)
  }
}

const intervalId = [null, null, null, null]

const getWithiInterval = (interval) => {
  getLastValue(1)
  getLastValue(2)
  getLastValue(3)
  getLastValue(4)
  intervalId[0] = setInterval(() => getLastValue(1), interval * 1000)
  intervalId[1] = setInterval(() => getLastValue(2), interval * 1000)
  intervalId[2] = setInterval(() => getLastValue(3), interval * 1000)
  intervalId[3] = setInterval(() => getLastValue(4), interval * 1000)
}

onMounted(() => getWithiInterval(3))

onUnmounted(() => {
  clearInterval(intervalId[0])
  clearInterval(intervalId[1])
  clearInterval(intervalId[2])
  clearInterval(intervalId[3])
})

provide('readings', readings)
</script>

<template>
  <div class="mnemo_box">
    <MnemonicDiagram />
  </div>
</template>

<style scoped>
.mnemo_box {
  /* background: red; */
  margin-left: 500px;
  margin-top: 160px;
  z-index: 0;
}
</style>
