<!-- <script setup>
import Chart from 'chart.js/auto'
import axios from 'axios'
import { onMounted, inject, ref, reactive } from 'vue'

var API_port = import.meta.env.VITE_API_ENDPOINT

const access_token = inject('access_token')

const full_power_values = ref([])
const labels_value = ref([1, 2, 3, 4, 5])
const date_values = ref([1, 2, 3, 4, 5])

const getFullPower = async () => {
  try {
    const { data } = await axios.get(
      `http://` +
        API_port +
        `/device/get_full_power/${device_value.value}/${date_value.value}/${time_1_value.value}/${time_2_value.value}`,
      {
        headers: { Authorization: access_token.value }
      }
    )
    full_power_values.value = data
    for (let i = 0; i < full_power_values.value.length; i++) {
      full_power_values.value[i].date_of_collection = full_power_values.value[i].date_of_collection
        .toString()
        .slice(11, 19)
    }
    labels_value.value = full_power_values.value.map((t) => t.full_power)
    date_values.value = full_power_values.value.map((t) => t.date_of_collection)
    return data
  } catch (err) {
    console.log(err)
  }
}

// const data = ref({})
// const config = ref({})

const device_value = ref(1)
const date_value = ref()
const time_1_value = ref('00:00:00')
const time_2_value = ref('23:59:59')

const data = {
  labels: date_values.value,
  datasets: [
    {
      label: '',
      data: labels_value.value,
      borderWidth: 3
    }
  ]
}

const config = {
  type: 'line',
  data: data,
  option: {}
}

const currentDate = new Date()
const year = currentDate.getFullYear()
const month = String(currentDate.getMonth() + 1).padStart(2, '0')
const day = String(currentDate.getDate()).padStart(2, '0')
console.log(year + '-' + month + '-' + day)
date_value.value = year + '-' + month + '-' + day
await getFullPower()
const myChart = new Chart(document.getElementById('myChart'), config)

// const getCurrentDate = async () => {
//   const currentDate = new Date()
//   const year = currentDate.getFullYear()
//   const month = String(currentDate.getMonth() + 1).padStart(2, '0')
//   const day = String(currentDate.getDate()).padStart(2, '0')
//   console.log(year + '-' + month + '-' + day)
//   date_value.value = year + '-' + month + '-' + day
//   await getFullPower()
//   myChart.value = new Chart(document.getElementById('myChart'), config.value)
// }

const updateChart = () => {
  const data = {
    labels: date_values.value,
    datasets: [
      {
        label: '',
        data: labels_value.value,
        borderWidth: 3
      }
    ]
  }
  myChart.data = data
  myChart.update()
  console.log('123123')
}

// const Rt = () => {
//   console.log(device_value.value)
//   console.log(date_value.value)
//   console.log(time_1_value.value)
//   console.log(time_2_value.value)
// }

// onMounted(() => getCurrentDate())
</script>

<template>
  <div class="main">
    <div class="input_main">
      <div class="input_box">
        <label for="mySelect">Устройство:</label>
        <select class="input_input" id="mySelect" v-model="device_value">
          <option value="">--Выберете--</option>
          <option value="1">Трансформатор 1</option>
          <option value="2">Трансформатор 2</option>
          <option value="3">Трансформатор 3</option>
          <option value="4">Трансформатор 4</option>
        </select>
      </div>
      <div class="datetime_input">
        <div class="input_box">
          <label for="time-date">Дата:</label>
          <input
            class="input_input"
            type="date"
            name="dateInput"
            id="time-date"
            v-model="date_value"
            required
          />
        </div>

        <div class="input_box">
          <label for="time-input_1">От:</label>
          <input
            class="input_input"
            type="time"
            id="time-input_1"
            name="time"
            step="1"
            v-model="time_1_value"
          />
        </div>

        <div class="input_box">
          <label for="time-input_2">До:</label>
          <input
            class="input_input"
            type="time"
            id="time-input_2"
            name="time"
            step="1"
            v-model="time_2_value"
          />
        </div>
        <div class="btn" @click="[getFullPower(), updateChart()]">Получить статистику</div>
      </div>
    </div>

    <div class="main_chart">
      <canvas id="myChart" width="300" height="100"></canvas>
    </div>
  </div>
</template>

<style scoped>
.but {
  background-color: blue;
  width: 100px;
  height: 100px;
}
.main {
  width: 100%;
}
label {
  color: white;
  margin-right: 10px;
}
.main_chart {
  width: 1000px;
}

.input_input {
  background: transparent;
  color: white;
  border: 2px solid #009485;
  border-radius: 15px;
  padding: 2px;
}

option {
  background: #009485;
}

.input_main {
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
}

.datetime_input {
  display: flex;
  width: 40%;
  justify-content: space-around;
}
input[type='time']::-webkit-calendar-picker-indicator {
  filter: invert(1); /* Инвертировать цвета */
}
input[type='date']::-webkit-calendar-picker-indicator {
  filter: invert(1); /* Инвертировать цвета */
}

.btn {
  border-radius: 8px;
  background: #009485;
  padding: 2px 10px 2px 10px;
  font-size: 17px;
  transition: 0.2s;
  color: white;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn:hover {
  background: #04786c;
  transition: 0.2s;
  transition: 0.2s;
}
</style> -->
