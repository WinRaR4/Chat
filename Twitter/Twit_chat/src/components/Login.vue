<template>
    <div>
        <input v-model="login" type="text" maxlength="12" placeholder="Ваш логинчик"/>
        <input v-model="password" type="password" maxlength="15" placeholder="Ваш паролик"/>
        <br>
        <br>
        <button @click="setLogin">Вход!</button>
    </div>
</template>

<script>
import $ from 'jQuery'

export default {
    name: "Login",
    data() {
        return {
            login: "",
            password: "",
        }
    },
    methods: {
        setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        sessionStorage.setItem('auth_token', response.data)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
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
        width: 2cm;
    }
    input {
        width: 3cm;
        border-width: 5px;
        text-rendering: geometricPrecision;
    }
</style>
