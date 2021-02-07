<template>
        <div class="dialog">
            <row v-for="dialog in dialogs" :key="dialog.id">
                <p>{{dialog.user.username}}</p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </row>
                <textarea full-width placeholder="Введите текст сообщения"></textarea>
                <button class="btn-send" round color="success" @click="sendMes">Отправить</button>
        </div>
</template>

<script>
import $ from 'jQuery'

    export default {
        name: "Dialog",
        props: ['id'],
        data() {
            return {
                dialogs: '',
                text: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
            setInterval(() => {
                this.loadDialog()
            }, 5000)
        },
        methods: {
            // Загрузка сообщений
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/dial/",
                    type: "GET",
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data
                    }
                })
            },
            // Отправка сообщения
            sendMes() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/dial/",
                    type: "POST",
                    data: {
                        room: 1,
                        text: this.text
                    },
                    success: (response) => {
                        this.loadDialog()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .dialog {
        border: 1px solid #000;
    }

    .btn-send {
        margin: 60px 0 0 15px;
    }
</style>
