<script setup>
import { ref, reactive, watch, inject } from 'vue'
import axios from 'axios'

// import { useFetch } from '@vueuse/core'
import { useRouter } from 'vue-router'

const router = useRouter()

var API_port = import.meta.env.VITE_API_ENDPOINT

const loginError = ref('')

const current_user = inject('current_user')
const access_token = inject('access_token')

const user = reactive({
  name: '',
  email: '',
  password: '',
  role: 'staff'
})

const dirtyFlag = reactive({
  name: false,
  email: false,
  password: false
})

const validationError = reactive({
  name: '',
  email: '',
  password: '',
  form: true
})

const validationForm = () => {
  if (
    validationError.name ||
    validationError.email ||
    validationError.password ||
    !user.email ||
    user.password < 8
  ) {
    validationError.form = true
  } else {
    validationError.form = false
  }
}

const validationEmail = () => {
  const re = /^\S+@\S+\.\S+$/
  if (!re.test(String(user.email).toLocaleLowerCase()) && dirtyFlag.email) {
    validationError.email = 'Некорректный email'
  } else {
    validationError.email = ''
  }
}

const validationPassword = () => {
  if (user.password.length < 8 && dirtyFlag.password) {
    validationError.password = 'Некорректный пароль. Минимальная длина пароля — 8 символов'
  } else {
    validationError.password = ''
  }
}

watch([() => dirtyFlag.email, () => user.email], validationEmail)
watch([() => dirtyFlag.password, () => user.password], validationPassword)

watch([() => dirtyFlag.email, () => user.email], validationForm)
watch([() => dirtyFlag.password, () => user.password], validationForm)

const getMe = async () => {
  try {
    const { data } = await axios.get(`http://` + API_port + `/auth/me`, {
      headers: { Authorization: access_token.value }
    })
    current_user.value = data
    localStorage.user = JSON.stringify(data)
  } catch (err) {
    console.log(err)
  }
}

const loginUser = async () => {
  // убирает перезагрузку страницы
  event.preventDefault()

  try {
    const { data } = await axios.post(`http://` + API_port + `/auth/login`, {
      email: user.email,
      password: user.password
    })
    access_token.value = data['access_token']
    localStorage.access_token = data['access_token']
    await getMe()
    router.push('/mnemo')
    return data
  } catch (err) {
    console.log(err)
    // loginError.value = err.response.data.detail
    loginError.value = 'Неверный email или пароль'
  }
}
</script>

<template>
  <form action="" class="registration_form">
    <h1>Вход</h1>

    <div class="input_box">
      <label class="label_name">Email</label>
      <input
        class="text_input"
        type="email"
        v-model="user.email"
        @blur="() => (dirtyFlag.email = true)"
      />
      <div class="error_box">{{ validationError.email }}</div>
    </div>

    <div class="input_box">
      <label class="label_name">Пароль</label>
      <input
        class="text_input"
        type="password"
        v-model="user.password"
        @blur="() => (dirtyFlag.password = true)"
      />
      <div class="error_box">{{ validationError.password }}</div>
    </div>
    <div class="login_error_box">{{ loginError }}</div>
    <button @click="loginUser" :disabled="validationError.form">Войти</button>
  </form>
</template>

<style scoped>
.label_name {
  display: block;
  color: aliceblue;
}
.label_role {
  margin-bottom: 10px;
}
h1 {
  font-size: 25px;
  margin-bottom: 20px;
  color: aliceblue;
}
.registration_form {
  display: flex;
  flex-direction: column;
  width: 520px;
  align-content: center;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

.input_box {
  margin-bottom: 10px;
  width: 100%;
}

.input_box:nth-child(5) {
  margin-bottom: 30px;
}
.text_input {
  border: 2px solid black;
  border-radius: 5px;
  padding: 4px 10px;
  width: 100%;
}

.text_input:hover {
  border: 2px solid #009485;
}

input:focus {
  outline: #009485;
  border-color: #009485;
}

input[type='radio'] {
  accent-color: #009485;
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

.error_box {
  height: 20px;
  color: rgb(255, 115, 115);
  font-size: 15px;
}

.login_error_box {
  height: 20px;
  color: rgb(255, 115, 115);
  font-size: 15px;
  margin-bottom: 10px;
}

form {
  /* background: #3bb4b4; */
  margin: 0 auto;
  margin-top: 200px;
}
</style>
