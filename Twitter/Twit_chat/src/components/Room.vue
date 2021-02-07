<template>
    <div>
        <br>
        <table border="20cm">
        <ul v-for="msg in messages" :key="msg.id">
            <h3 v-for="ms in msg" :key="ms.id">
                {{ms.user.username}} <br>
                <small>{{ms.text}}</small>
                <hr>
            </h3>
        </ul>
        <textarea v-model="text" full-width placeholder="Введите текст сообщения"></textarea>
        <button class="btn-send" round color="success" @click="sendMes">Отправить</button>
        </table>
    </div>
</template>

<script>
    import $ from 'jQuery'

    export default {
        name: "Room",
        data() {
            return {
                messages: '',
                text: '',
            }
        },
        components: {

        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRoom()
            setInterval(() => {
                this.loadRoom()
            }, 5000)
        },
        methods: {
            // Загружаю список комнат
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/msg/",
                    type: "GET",
                    success: (response) => {
                        this.messages = response
                        console.log(response)
                    }
                })
            },
            openDialog(id) {
                // this.$emit("openDialog", id)
                this.$router.push({name: 'dial', params: {id: id}})
            },
            sendMes() {
                $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
                $.ajax({
                    url: "http://127.0.0.1:8000/api/msg/",
                    type: "POST",
                    data: {
                        
                        text: this.text, 
                    },
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
            // Создание комнаты
        }
    }
</script>

<style scoped>
    h3 {
        border-block-color: aqua;
        border-bottom: 3cm;
    }

    .rooms-list {
        margin: 0 1000px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
    table {
        background-color: rgb(175, 166, 162);
    }
</style>
