<script setup>
import { reactive, provide, inject, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

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
readings[id - 1].s = data.full_power readings[id - 1].p = data.active_power readings[id - 1].q =
data.reactive_power readings[id - 1].u = data.voltage readings[id - 1].i = data.amperage readings[id
- 1].cos = data.power_factor
<template>
  <div class="mnemo_box">
    <!-- <MnemonicDiagram /> -->
    <img src="/mnemo.svg" class="mnemo_img" alt="" />
    <div class="value_box v1">
      <p><span>S =</span> {{ readings[0].s }} <span>ВА</span></p>
      <p><span>P =</span> {{ readings[0].p }} <span>Вт</span></p>
      <p><span>Q =</span> {{ readings[0].q }} <span>вар</span></p>
      <p><span>U =</span> {{ readings[0].u }} <span>В</span></p>
      <p><span>I =</span> {{ readings[0].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[0].cos }}</p>
    </div>
    <div class="value_box v2">
      <p><span>S =</span> {{ readings[1].s }} <span>ВА</span></p>
      <p><span>P =</span> {{ readings[1].p }} <span>Вт</span></p>
      <p><span>Q =</span> {{ readings[1].q }} <span>вар</span></p>
      <p><span>U =</span> {{ readings[1].u }} <span>В</span></p>
      <p><span>I =</span> {{ readings[1].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[1].cos }}</p>
    </div>
    <div class="value_box v3">
      <p><span>S =</span> {{ readings[2].s }} <span>ВА</span></p>
      <p><span>P =</span> {{ readings[2].p }} <span>Вт</span></p>
      <p><span>Q =</span> {{ readings[2].q }} <span>вар</span></p>
      <p><span>U =</span> {{ readings[2].u }} <span>В</span></p>
      <p><span>I =</span> {{ readings[2].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[2].cos }}</p>
    </div>
    <div class="value_box v4">
      <p><span>S =</span> {{ readings[3].s }} <span>ВА</span></p>
      <p><span>P =</span> {{ readings[3].p }} <span>Вт</span></p>
      <p><span>Q =</span> {{ readings[3].q }} <span>вар</span></p>
      <p><span>U =</span> {{ readings[3].u }} <span>В</span></p>
      <p><span>I =</span> {{ readings[3].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[3].cos }}</p>
    </div>

    <div class="switch s1_1">123</div>
  </div>
</template>

<style scoped>
.switch {
  background: #00d445;
  width: 26px;
  height: 26px;
  position: relative;
  z-index: 100;
  left: -168px;
  top: -21px;
}
.mnemo_box {
  /* background: #00d445; */
  margin-top: 160px;
  /* margin-right: 200px; */
  margin-left: 500px;
  position: relative;
}
.mnemo_img {
  transform: scale(1.7);
}

.value_box {
  border: 2px solid black;
  width: 100px;
  z-index: 2;
  padding: 2px;
  font-size: 13px;
}
.v1 {
  position: fixed;
  left: 277px;
  top: 395px;
}
.v2 {
  position: fixed;
  left: 557px;
  top: 440px;
}
.v3 {
  position: fixed;
  left: 1090px;
  top: 460px;
}
.v4 {
  position: fixed;
  left: 1430px;
  top: 460px;
}

.value_box p {
  margin-top: -5px;
  color: #00d445;
}
.value_box span {
  color: #f2a42f;
}
</style>
