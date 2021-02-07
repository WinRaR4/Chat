<template>
    <div>
        <input v-model="username" type="text" maxlength="12" placeholder="Ваш логинчик"/>
        <input v-model="password" type="password" maxlength="15" placeholder="Ваш паролик"/>
        <input v-model="email" type="email" maxlength="25" placeholder="А как же почта?)"/>
        <br>
        <br>
        <button @click="regMe">Зарегистрировать меня!</button>
    </div>
</template>

<script>
import $ from 'jQuery'

export default {
    name: "Registrate",
    data() {
        return {
            username: "",
            password: "",
            email: "",
        }
    },
    methods: {
        regMe() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password,
                        email: this.email,
                    },
                    success: (response) => {
                        sessionStorage.setItem('auth_token', response.data)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert(response.statusText)
                        }
                    }
                })
            },
    }
}
</script>

<style scoped>
    button {
        border-top-color: teal;
        border-left-color: teal;
        border-right-color: teal;
        border-bottom-color: teal;
        width: 4cm;
    }
    input {
        width: 3cm;
        border-width: 5px;
        text-rendering: geometricPrecision;
    }
</style>
