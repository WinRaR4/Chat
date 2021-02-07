<template>
    <div>
        <h1>Простой чатик!</h1>
        <button flat slot="right" v-if="!auth" @click="log">Вход</button>
        <button flat slot="right" v-if="!auth" @click="reg">Регистрация</button>
        <button flat slot="right" v-else @click="logout">Выход</button>
        <br>
        <Room v-if="auth"></Room>
    </div>
</template>

<script>
import Room from './Room.vue'
import Registrate from './Registrate.vue'

export default {
    name: "Home",
    data() {
      return {

      }
    },
    components: {
        Room,
        Registrate,
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        },
    },
    methods: {
            log() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = ''
            },
            reg() {
                this.$router.push({name: "register"})
            }
            // Открываю диалог
            // openDialog(id) {
                // this.dialog.id = id
                // this.dialog.show = true
            // }
        },
}
</script>

<style scoped>
button {
        border-top-color: teal;
        border-left-color: teal;
        border-right-color: teal;
        border-bottom-color: teal;
        width: 2.5cm;
    }
input {
        width: 3cm;
        border-width: 5px;
        text-rendering: geometricPrecision;
    }
h3 {
    text-shadow: lightcoral;
}
</style>
