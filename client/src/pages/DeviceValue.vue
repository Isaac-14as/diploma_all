<script setup>
import axios from 'axios'
import { inject, ref, onMounted, watch } from 'vue'

var API_port = import.meta.env.VITE_API_ENDPOINT

const access_token = inject('access_token')
// const current_user = inject('current_user')

const device_value = ref([])
const main_device_value = ref([])
const device_name = ref('')

const getValueDevice = async () => {
  date_value.value = null
  time_1_value.value = null
  time_2_value.value = null
  const device_id = window.location.toString().split('/').reverse()[0]
  try {
    const { data } = await axios({
      method: 'get',
      url: `http://` + API_port + `/device/get_all_value_device_by_id/${device_id}`,
      headers: { Authorization: access_token.value }
    })
    device_value.value = data.reverse()
    for (let i = 0; i < device_value.value.length; i++) {
      const data = device_value.value[i].date_of_collection.slice(0, 10)
      const time = device_value.value[i].date_of_collection.slice(11, 19)
      device_value.value[i].date_of_collection = data + ' (' + time + ')'
    }
    main_device_value.value = device_value.value
    console.log(device_value.value)
    return data
  } catch (err) {
    console.log(err)
  }
}

const getDevice = async () => {
  const device_id = window.location.toString().split('/').reverse()[0]
  try {
    const { data } = await axios({
      method: 'get',
      url: `http://` + API_port + `/device/get_device_by_id/${device_id}`,
      headers: { Authorization: access_token.value }
    })
    device_name.value = data.name
    console.log(device_name.value)
    return data
  } catch (err) {
    console.log(err)
  }
}
onMounted(getDevice)
onMounted(getValueDevice)

const search_text = ref('')

const onChangeSearchInput = async () => {
  const device_value_search = []

  if (search_text.value === '') {
    main_device_value.value = device_value.value
  }
  for (let i = 0; i < device_value.value.length; i++) {
    let full_power_search =
      device_value.value[i].full_power.toString().indexOf(search_text.value) != -1
    let active_power_search =
      device_value.value[i].active_power
        .toString()
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    let reactive_power_search =
      device_value.value[i].reactive_power
        .toString()
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    let voltage_search =
      device_value.value[i].voltage
        .toString()
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    let amperage_search =
      device_value.value[i].amperage
        .toString()
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    let power_factor_search =
      device_value.value[i].power_factor
        .toString()
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    let date_of_collection_search =
      device_value.value[i].date_of_collection
        .toLowerCase()
        .indexOf(search_text.value.toLowerCase()) != -1
    if (
      full_power_search ||
      active_power_search ||
      reactive_power_search ||
      voltage_search ||
      amperage_search ||
      power_factor_search ||
      date_of_collection_search
    ) {
      device_value_search.push(device_value.value[i])
    }
  }
  main_device_value.value = device_value_search
  console.log(main_device_value.value)
}
const date_value = ref(null)
const time_1_value = ref(null)
const time_2_value = ref(null)
const getLogDateTime = async () => {
  const device_id = window.location.toString().split('/').reverse()[0]
  if (date_value.value && time_1_value.value && time_2_value.value) {
    try {
      const { data } = await axios.get(
        `http://` +
          API_port +
          `/device/get_value_by_date_time/${device_id}/${date_value.value}/${time_1_value.value}/${time_2_value.value}`,
        {
          headers: { Authorization: access_token.value }
        }
      )
      console.log(data)
      device_value.value = data.reverse()
      for (let i = 0; i < device_value.value.length; i++) {
        const data = device_value.value[i].date_of_collection.slice(0, 10)
        const time = device_value.value[i].date_of_collection.slice(11, 19)
        device_value.value[i].date_of_collection = data + ' (' + time + ')'
      }
      main_device_value.value = device_value.value
    } catch (err) {
      console.log(err)
    }
  }
}

watch([() => date_value.value, () => time_1_value.value, () => time_2_value.value], getLogDateTime)
</script>

<template>
  <div class="list_main">
    <div class="title_search">
      <div class="title">{{ device_name }}</div>
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
      </div>
      <div class="left_header">
        <input class="search" type="text" @input="onChangeSearchInput" v-model="search_text" />
        <div class="update" @click="getValueDevice">Обновить</div>
      </div>
    </div>

    <div class="list_name">
      <div class="box">
        <div class="info headers">
          <div class="active_power h">Активная мощность</div>
          <div class="reactive_power h">Реактивная мощность</div>
          <div class="full_power h">Полная мощность</div>
          <div class="amperage h">Сила тока</div>
          <div class="voltage h">Напряжение</div>
          <div class="power_factor h">Коэффициент мощности</div>
          <div class="date_of_collection header_time h">Дата/время</div>
        </div>
      </div>
    </div>

    <div class="list">
      <div class="box" v-for="value in main_device_value" :key="value.id">
        <div class="info">
          <div class="active_power">{{ value.active_power }}</div>
          <div class="reactive_power">{{ value.reactive_power }}</div>
          <div class="full_power">{{ value.full_power }}</div>
          <div class="amperage">{{ value.amperage }}</div>
          <div class="voltage">{{ value.voltage }}</div>
          <div class="power_factor">{{ value.power_factor }}</div>
          <div class="date_of_collection">{{ value.date_of_collection }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.h {
  align-content: center;
}
.left_header {
  display: flex;
  justify-content: space-between;
  width: 40%;
}
.button_box {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 20px;
}
.update {
  border-radius: 8px;
  background: #009485;
  padding: 2px 10px 2px 10px;
  font-size: 17px;
  transition: 0.2s;
  color: white;
  cursor: pointer;
}

.update:hover {
  background: #04786c;
  transition: 0.2s;
  transition: 0.2s;
}

.title_search {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}
.title {
  margin-bottom: 10px;
  font-size: 20px;
}

.search {
  height: 30px;
  width: 350px;
  border: 2px solid black;
  border-radius: 5px;
  padding: 4px 10px;
  color: #000000;
}

.search:hover {
  border: 2px solid #009485;
}

.search:focus {
  outline: #009485;
  border-color: #009485;
}

.list_main {
  width: 65%;
  margin-left: 25px;
  color: white;
  margin-top: 30px;
  margin: 0 auto;
  margin-top: 30px;
}
.is_active {
  border-left: 1px solid white;
  padding-left: 10px;
  width: 250px;
}

.list {
  overflow: scroll;
  overflow-x: hidden;
  height: 650px;
}
.list_name {
  margin-bottom: 20px;
}

.box {
  border: 1px solid white;
  width: 98%;
}
.info {
  display: flex;
}

.list::-webkit-scrollbar {
  width: 3px;
  height: 15px;
}

.list::-webkit-scrollbar-thumb {
  background: #009485;
  border-radius: 1px;
}

.list::-webkit-scrollbar-track:vertical {
  background-color: rgb(69, 67, 67);
  box-shadow: inset 0 0 2px 2px rgb(87, 86, 86);
}

.active_power {
  width: 15%;
  border-right: 1px solid white;
  padding-left: 10px;
}
.reactive_power {
  width: 15%;
  border-right: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.full_power {
  width: 13%;
  border-right: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.amperage {
  width: 10%;
  border-right: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.voltage {
  width: 10%;
  border-right: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.power_factor {
  width: 15%;
  border-right: 1px solid white;
  padding-left: 10px;
  padding-right: 10px;
}
.date_of_collection {
  width: 20%;
  padding-left: 10px;
  padding-right: 10px;
}

button {
  border-radius: 8px;
  background: #009485;
  padding: 15px;
  font-size: 17px;
  transition: 0.2s;
  color: white;
}

button:hover {
  background: #04786c;
  transition: 0.2s;
  transition: 0.2s;
}
button:disabled {
  background: #5f6464;
  transition: 0.2s;
  transition: 0.2s;
}

.input_input {
  background: transparent;
  color: white;
  border: 2px solid #009485;
  border-radius: 15px;
  padding: 2px;
}

option {
  background: #989897;
  background: #009485;
}
label {
  color: white;
  margin-right: 10px;
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
</style>
