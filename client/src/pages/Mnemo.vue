<script setup>
import { reactive, inject, onMounted, onUnmounted, ref } from 'vue'
import axios from 'axios'

const access_token = inject('access_token')
var API_port = import.meta.env.VITE_API_ENDPOINT

const current_user = inject('current_user')
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

const devices = ref()
const getAllDevices = async () => {
  try {
    const { data } = await axios.get(`http://` + API_port + `/device/get_all_devices`, {
      headers: { Authorization: access_token.value }
    })
    devices.value = data.sort((a, b) => a.id - b.id)
    console.log(devices.value[4].is_active)
    return data
  } catch (err) {
    console.log(err)
  }
}

const deviceSwitchOff = async (id) => {
  try {
    const { data } = await axios({
      method: 'patch',
      url: `http://` + API_port + `/device/device_switch_off/${id}`,
      headers: { Authorization: access_token.value }
    })
    // изменение одного из иустройст на стороне клиента
    let device_change = devices.value.find((item) => item.id === id)
    device_change.is_active = false
    devices.value[devices.value.indexOf(devices.value.find((item) => item.id === id))] =
      device_change
    info_text.value = ''
    modelInfoOff()
    return data
  } catch (err) {
    console.log(err)
  }
}

const deviceTurnOn = async (id) => {
  try {
    const { data } = await axios({
      method: 'patch',
      url: `http://` + API_port + `/device/device_turn_on/${id}`,
      headers: { Authorization: access_token.value }
    })
    // изменение одного из иустройст на стороне клиента
    let device_change = devices.value.find((item) => item.id === id)
    device_change.is_active = true
    devices.value[devices.value.indexOf(devices.value.find((item) => item.id === id))] =
      device_change
    info_text.value = ''
    modelInfoOff()
    return data
  } catch (err) {
    console.log(err)
  }
}

const addManagementLog = async (device_id, action) => {
  try {
    const { data } = await axios({
      method: 'post',
      url: `http://` + API_port + `/device/add_management_log`,
      headers: { Authorization: access_token.value },
      data: {
        info: info_text.value,
        action: action,
        user_id: current_user.value.id,
        device_id: device_id
      }
    })
    return data
  } catch (err) {
    console.log(err)
  }
}
const info_text = ref('')
const device_action = ref('')
const model_flag = ref(false)
const modelInfoOn = async (device) => {
  device_action.value = device
  model_flag.value = true
}

const modelInfoOff = async () => {
  model_flag.value = false
}

onMounted(() => getAllDevices())
</script>
<template>
  <div class="mnemo_box">
    <!-- <MnemonicDiagram /> -->
    <img src="/mnemo.svg" class="mnemo_img" alt="" />
    <div class="value_box v1">
      <p><span>S =</span> {{ readings[0].s }} <span>МВА</span></p>
      <p><span>P =</span> {{ readings[0].p }} <span>МВт</span></p>
      <p><span>Q =</span> {{ readings[0].q }} <span>МВАр</span></p>
      <p><span>U =</span> {{ readings[0].u }} <span>кВ</span></p>
      <p><span>I =</span> {{ readings[0].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[0].cos }}</p>
    </div>
    <div class="value_box v2">
      <p><span>S =</span> {{ readings[1].s }} <span>МВА</span></p>
      <p><span>P =</span> {{ readings[1].p }} <span>МВт</span></p>
      <p><span>Q =</span> {{ readings[1].q }} <span>МВАр</span></p>
      <p><span>U =</span> {{ readings[1].u }} <span>кВ</span></p>
      <p><span>I =</span> {{ readings[1].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[1].cos }}</p>
    </div>
    <div class="value_box v3">
      <p><span>S =</span> {{ readings[2].s }} <span>МВА</span></p>
      <p><span>P =</span> {{ readings[2].p }} <span>МВт</span></p>
      <p><span>Q =</span> {{ readings[2].q }} <span>МВАр</span></p>
      <p><span>U =</span> {{ readings[2].u }} <span>кВ</span></p>
      <p><span>I =</span> {{ readings[2].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[2].cos }}</p>
    </div>
    <div class="value_box v4">
      <p><span>S =</span> {{ readings[3].s }} <span>МВА</span></p>
      <p><span>P =</span> {{ readings[3].p }} <span>МВт</span></p>
      <p><span>Q =</span> {{ readings[3].q }} <span>МВАр</span></p>
      <p><span>U =</span> {{ readings[3].u }} <span>кВ</span></p>
      <p><span>I =</span> {{ readings[3].i }} <span>А</span></p>
      <p><span>cosφ =</span> {{ readings[3].cos }}</p>
    </div>

    <div
      v-if="devices && devices[4] && devices[4].is_active"
      class="switch_1 s1_1 s1_t"
      @click="modelInfoOn(devices[4])"
    ></div>
    <div v-else class="switch_1 s1_1" @click="modelInfoOn(devices[4])"></div>

    <div
      v-if="devices && devices[5] && devices[5].is_active"
      class="switch_1 s1_2 s1_t"
      @click="modelInfoOn(devices[5])"
    ></div>
    <div v-else class="switch_1 s1_2" @click="modelInfoOn(devices[5])"></div>

    <div
      v-if="devices && devices[6] && devices[6].is_active"
      class="switch_1 s1_3 s1_t"
      @click="modelInfoOn(devices[6])"
    ></div>
    <div v-else class="switch_1 s1_3" @click="modelInfoOn(devices[6])"></div>

    <div
      v-if="devices && devices[7] && devices[7].is_active"
      class="switch_1 s1_4 s1_t"
      @click="modelInfoOn(devices[7])"
    ></div>
    <div v-else class="switch_1 s1_4" @click="modelInfoOn(devices[7])"></div>

    <div
      v-if="devices && devices[8] && devices[8].is_active"
      class="switch_2 s2_1 s2_t"
      @click="modelInfoOn(devices[8])"
    ></div>
    <div v-else class="switch_2 s2_1" @click="modelInfoOn(devices[8])"></div>

    <div
      v-if="devices && devices[9] && devices[9].is_active"
      class="switch_2 s2_2 s2_t"
      @click="modelInfoOn(devices[9])"
    ></div>
    <div v-else class="switch_2 s2_2" @click="modelInfoOn(devices[9])"></div>

    <div
      v-if="devices && devices[10] && devices[10].is_active"
      class="switch_2 s2_3 s2_t"
      @click="modelInfoOn(devices[10])"
    ></div>
    <div v-else class="switch_2 s2_3" @click="modelInfoOn(devices[10])"></div>

    <div
      v-if="devices && devices[11] && devices[11].is_active"
      class="switch_2 s2_4 s2_t"
      @click="modelInfoOn(devices[11])"
    ></div>
    <div v-else class="switch_2 s2_4" @click="modelInfoOn(devices[11])"></div>

    <div
      v-if="devices && devices[12] && devices[12].is_active"
      class="switch_2 s2_5 s2_t"
      @click="modelInfoOn(devices[12])"
    ></div>
    <div v-else class="switch_2 s2_5" @click="modelInfoOn(devices[12])"></div>

    <div
      v-if="devices && devices[13] && devices[13].is_active"
      class="switch_2 s2_6 s2_t"
      @click="modelInfoOn(devices[13])"
    ></div>
    <div v-else class="switch_2 s2_6" @click="modelInfoOn(devices[13])"></div>

    <div
      v-if="devices && devices[14] && devices[14].is_active"
      class="switch_2 s2_7 s2_t"
      @click="modelInfoOn(devices[14])"
    ></div>
    <div v-else class="switch_2 s2_7" @click="modelInfoOn(devices[14])"></div>

    <div
      v-if="devices && devices[15] && devices[15].is_active"
      class="switch_2 s2_8 s2_t"
      @click="modelInfoOn(devices[15])"
    ></div>
    <div v-else class="switch_2 s2_8" @click="modelInfoOn(devices[15])"></div>

    <div
      v-if="devices && devices[16] && devices[16].is_active"
      class="switch_3 s3_1 s3_t"
      @click="modelInfoOn(devices[16])"
    ></div>
    <div v-else class="switch_3 s3_1" @click="modelInfoOn(devices[16])"></div>

    <div
      v-if="devices && devices[17] && devices[17].is_active"
      class="switch_3 s3_2 s3_t"
      @click="modelInfoOn(devices[17])"
    ></div>
    <div v-else class="switch_3 s3_2" @click="modelInfoOn(devices[17])"></div>

    <div
      v-if="devices && devices[18] && devices[18].is_active"
      class="switch_3 s3_3 s3_t"
      @click="modelInfoOn(devices[18])"
    ></div>
    <div v-else class="switch_3 s3_3" @click="modelInfoOn(devices[18])"></div>

    <div
      v-if="devices && devices[19] && devices[19].is_active"
      class="switch_3 s3_4 s3_t"
      @click="modelInfoOn(devices[19])"
    ></div>
    <div v-else class="switch_3 s3_4" @click="modelInfoOn(devices[19])"></div>

    <div
      v-if="devices && devices[20] && devices[20].is_active"
      class="switch_3 s3_5 s3_t"
      @click="modelInfoOn(devices[20])"
    ></div>
    <div v-else class="switch_3 s3_5" @click="modelInfoOn(devices[20])"></div>

    <div
      v-if="devices && devices[21] && devices[21].is_active"
      class="switch_3 s3_6 s3_t"
      @click="modelInfoOn(devices[21])"
    ></div>
    <div v-else class="switch_3 s3_6" @click="modelInfoOn(devices[21])"></div>

    <div
      v-if="devices && devices[22] && devices[22].is_active"
      class="switch_3 s3_7 s3_t"
      @click="modelInfoOn(devices[22])"
    ></div>
    <div v-else class="switch_3 s3_7" @click="modelInfoOn(devices[22])"></div>

    <div
      v-if="devices && devices[23] && devices[23].is_active"
      class="switch_3 s3_8 s3_t"
      @click="modelInfoOn(devices[23])"
    ></div>
    <div v-else class="switch_3 s3_8" @click="modelInfoOn(devices[23])"></div>

    <div
      v-if="devices && devices[24] && devices[24].is_active"
      class="switch_3 s3_9 s3_t"
      @click="modelInfoOn(devices[24])"
    ></div>
    <div v-else class="switch_3 s3_9" @click="modelInfoOn(devices[24])"></div>

    <div
      v-if="devices && devices[25] && devices[25].is_active"
      class="switch_3 s3_10 s3_t"
      @click="modelInfoOn(devices[25])"
    ></div>
    <div v-else class="switch_3 s3_10" @click="modelInfoOn(devices[25])"></div>

    <div
      v-if="devices && devices[26] && devices[26].is_active"
      class="switch_3 s3_11 s3_t"
      @click="modelInfoOn(devices[26])"
    ></div>
    <div v-else class="switch_3 s3_11" @click="modelInfoOn(devices[26])"></div>

    <div
      v-if="devices && devices[27] && devices[27].is_active"
      class="switch_3 s3_12 s3_t"
      @click="modelInfoOn(devices[27])"
    ></div>
    <div v-else class="switch_3 s3_12" @click="modelInfoOn(devices[27])"></div>

    <div
      v-if="devices && devices[28] && devices[28].is_active"
      class="switch_3 s3_13 s3_t"
      @click="modelInfoOn(devices[28])"
    ></div>
    <div v-else class="switch_3 s3_13" @click="modelInfoOn(devices[28])"></div>

    <div
      v-if="devices && devices[29] && devices[29].is_active"
      class="switch_3 s3_14 s3_t"
      @click="modelInfoOn(devices[29])"
    ></div>
    <div v-else class="switch_3 s3_14" @click="modelInfoOn(devices[29])"></div>

    <div
      v-if="devices && devices[30] && devices[30].is_active"
      class="switch_3 s3_15 s3_t"
      @click="modelInfoOn(devices[30])"
    ></div>
    <div v-else class="switch_3 s3_15" @click="modelInfoOn(devices[30])"></div>

    <div
      v-if="devices && devices[31] && devices[31].is_active"
      class="switch_3 s3_16 s3_t"
      @click="modelInfoOn(devices[31])"
    ></div>
    <div v-else class="switch_3 s3_16" @click="modelInfoOn(devices[31])"></div>

    <div
      v-if="devices && devices[32] && devices[32].is_active"
      class="switch_4 s4_1 s4_t"
      @click="modelInfoOn(devices[32])"
    ></div>
    <div v-else class="switch_4 s4_1" @click="modelInfoOn(devices[32])"></div>

    <div
      v-if="devices && devices[33] && devices[33].is_active"
      class="switch_4 s4_2 s4_t"
      @click="modelInfoOn(devices[33])"
    ></div>
    <div v-else class="switch_4 s4_2" @click="modelInfoOn(devices[33])"></div>

    <div
      v-if="devices && devices[34] && devices[34].is_active"
      class="switch_4 s4_3 s4_t"
      @click="modelInfoOn(devices[34])"
    ></div>
    <div v-else class="switch_4 s4_3" @click="modelInfoOn(devices[34])"></div>

    <div
      v-if="devices && devices[35] && devices[35].is_active"
      class="switch_4 s4_4 s4_t"
      @click="modelInfoOn(devices[35])"
    ></div>
    <div v-else class="switch_4 s4_4" @click="modelInfoOn(devices[35])"></div>

    <div
      v-if="devices && devices[36] && devices[36].is_active"
      class="switch_4 s4_5 s4_t"
      @click="modelInfoOn(devices[36])"
    ></div>
    <div v-else class="switch_4 s4_5" @click="modelInfoOn(devices[36])"></div>

    <div
      v-if="devices && devices[37] && devices[37].is_active"
      class="switch_4 s4_6 s4_t"
      @click="modelInfoOn(devices[37])"
    ></div>
    <div v-else class="switch_4 s4_6" @click="modelInfoOn(devices[37])"></div>

    <div v-if="model_flag" class="blur"></div>
    <div v-if="model_flag" class="model_window">
      <div class="title_model">
        Причинана
        <p v-if="device_action.is_active">выключения</p>
        <p v-else>включения</p>
        <p>устройства</p>
        <p>"{{ device_action.name }}":</p>
      </div>
      <textarea
        class="test_info"
        placeholder="Опишите причину действия..."
        v-model="info_text"
      ></textarea>
      <div class="button_box">
        <button @click="modelInfoOff">Отмена</button>
        <button
          v-if="device_action.is_active"
          @click="
            [deviceSwitchOff(device_action.id), addManagementLog(device_action.id, 'Выключение')]
          "
        >
          Выключить
        </button>
        <button
          v-else
          @click="[deviceTurnOn(device_action.id), addManagementLog(device_action.id), 'Включение']"
        >
          Включить
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.switch_1 {
  width: 26px;
  height: 26px;
  z-index: 100;
  cursor: pointer;
}
.switch_2 {
  width: 27px;
  height: 27px;
  z-index: 100;
  cursor: pointer;
}

.switch_3 {
  width: 18px;
  height: 18px;
  z-index: 100;
  cursor: pointer;
}
.switch_4 {
  width: 25px;
  height: 25px;
  z-index: 100;
  cursor: pointer;
}
.s1_t {
  background: #ff0d00;
}

.s2_t {
  background: #e0e027;
}
.s3_t {
  background: #7601ad;
}
.s4_t {
  background: #00a5ce;
}
.s1_1 {
  position: absolute;
  z-index: 100;
  left: 9.9%;
  top: 18%;
}

.s1_2 {
  position: absolute;
  z-index: 100;
  left: 9.9%;
  top: 24.5%;
}

.s1_3 {
  position: absolute;
  z-index: 100;
  left: 26.5%;
  top: 18%;
}

.s1_4 {
  position: absolute;
  z-index: 100;
  left: 26.5%;
  top: 24.5%;
}

.s2_1 {
  position: absolute;
  z-index: 100;
  left: 8.6%;
  top: 75.3%;
}

.s2_2 {
  position: absolute;
  z-index: 100;
  left: 13.4%;
  top: 75.3%;
}
.s2_3 {
  position: absolute;
  z-index: 100;
  left: 19.9%;
  top: 75.3%;
}
.s2_4 {
  position: absolute;
  z-index: 100;
  left: 26.4%;
  top: 75.3%;
}

.s2_5 {
  position: absolute;
  z-index: 100;
  left: 32.1%;
  top: 75.3%;
}

.s2_6 {
  position: absolute;
  z-index: 100;
  left: 38.5%;
  top: 75.3%;
}

.s2_7 {
  position: absolute;
  z-index: 100;
  left: 45%;
  top: 75.3%;
}

.s2_8 {
  position: absolute;
  z-index: 100;
  left: 51.5%;
  top: 75.3%;
}
.s3_1 {
  position: absolute;
  z-index: 100;
  left: 32.79%;
  top: 22%;
}

.s3_2 {
  position: absolute;
  z-index: 100;
  left: 37.6%;
  top: 22%;
}
.s3_3 {
  position: absolute;
  z-index: 100;
  left: 42.5%;
  top: 22%;
}

.s3_4 {
  position: absolute;
  z-index: 100;
  left: 46.5%;
  top: 22%;
}

.s3_5 {
  position: absolute;
  z-index: 100;
  left: 50.2%;
  top: 22%;
}

.s3_6 {
  position: absolute;
  z-index: 100;
  left: 53.4%;
  top: 22%;
}

.s3_7 {
  position: absolute;
  z-index: 100;
  left: 58.2%;
  top: 22%;
}

.s3_8 {
  position: absolute;
  z-index: 100;
  left: 62.7%;
  top: 22%;
}

.s3_9 {
  position: absolute;
  z-index: 100;
  left: 66.3%;
  top: 22%;
}

.s3_10 {
  position: absolute;
  z-index: 100;
  left: 70%;
  top: 22%;
}
.s3_11 {
  position: absolute;
  z-index: 100;
  left: 74.4%;
  top: 22%;
}

.s3_12 {
  position: absolute;
  z-index: 100;
  left: 78.9%;
  top: 22%;
}

.s3_13 {
  position: absolute;
  z-index: 100;
  left: 82.4%;
  top: 22%;
}

.s3_14 {
  position: absolute;
  z-index: 100;
  left: 86.6%;
  top: 22%;
}
.s3_15 {
  position: absolute;
  z-index: 100;
  left: 91%;
  top: 22%;
}
.s3_16 {
  position: absolute;
  z-index: 100;
  left: 95%;
  top: 22%;
}

.s4_1 {
  position: absolute;
  z-index: 100;
  left: 64.83%;
  top: 75.39%;
}

.s4_2 {
  position: absolute;
  z-index: 100;
  left: 70.07%;
  top: 75.39%;
}
.s4_3 {
  position: absolute;
  z-index: 100;
  left: 75.35%;
  top: 75.39%;
}
.s4_4 {
  position: absolute;
  z-index: 100;
  left: 80.58%;
  top: 75.39%;
}
.s4_5 {
  position: absolute;
  z-index: 100;
  left: 87.1%;
  top: 75.39%;
}
.s4_6 {
  position: absolute;
  z-index: 100;
  left: 92.35%;
  top: 75.39%;
}

.v1 {
  position: absolute;
  left: 6.5%;
  top: 39%;
}
.v2 {
  position: absolute;
  left: 23.5%;
  top: 45%;
}
.v3 {
  position: absolute;
  left: 56%;
  top: 47%;
}
.v4 {
  position: absolute;
  left: 76%;
  top: 47%;
}

.mnemo_box {
  margin-left: 200px;
  position: relative;
  width: 1650px;
  height: 830px;
  border: 2px solid #333333;
  display: flex;
}

.value_box {
  width: 103px;
  z-index: 2;
  padding: 2px;
  font-size: 13px;
}

.value_box p {
  margin-top: -5px;
  color: #00d445;
}
.value_box span {
  color: #f2a42f;
}

.blur {
  position: fixed;
  background: #000000;
  left: 0;
  top: 0;
  z-index: 100;
  width: 100%;
  height: 100%;
  opacity: 0.7;
}

.model_window {
  position: absolute;
  left: 33%;
  top: 30%;
  width: 550px;
  height: 350px;
  background: #1c1c1c;
  border: #009485 solid 2px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 300;
}

.title_model {
  color: white;
  background: #009485;
  text-align: center;
  font-size: 17px;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 100%;
}
.title_model p {
  display: inline;
  margin-right: 5px;
}

.test_info {
  padding: 10px;
  width: 85%;
  height: 50%;
  border: 2px solid black;
  border-radius: 5px;
  margin-top: 10px;
}

.test_info:hover {
  border: 2px solid #009485;
}

.test_info:focus {
  outline: #009485;
  border-color: #009485;
}

.button_box {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 20px;
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
</style>
