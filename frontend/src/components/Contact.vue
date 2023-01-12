<template>
<div id="contact_with_me" class="relative grid gap-4 grid-cols-3 grid-rows-3 px-20 w-full h-96 bg-[url('/src/assets/tree_leaves.jpg')] bg-cover">
    <div class="row-start-2 col-span-2 text-white px-10">
        <span class="text-4xl">Contacts</span>
        <p class="font-bold">Email: <span class="text-green-200">kalmatkenesary1@gmail.com</span></p>
        <p class="font-bold">Telegram: <span class="text-green-200">@NumFog</span></p>
    </div>

    <form @submit.prevent="sendData" class="col-start-2 row-start-2">
        <div class="grid gap-4 grid-cols-2">
            <input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500" type="text" placeholder="name" v-model="name"/>
            <input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500" type="email" placeholder="email" v-model="email">
            <input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded col-span-2 py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500" type="text" placeholder="description" v-model="description"><br/>
            <button class="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded" type="submit">
                send
            </button>
        </div>
    </form>
    <div v-if="alertShow" class="absolute bottom-0 left-0 ml-10 mb-10 py-2 px-4 rounded font-bold grid justify-center content-center bg-green-700 text-white">
        <span>Success send!</span>
    </div>
</div>

</template>

<script>
import axios from 'axios'

export default {
    name: "Contact",
    data() {
        return {
            name: '',
            email: '',
            description: '',
            alertShow: false,
        }
    },
    methods: {
        sendData(e) {
            let postBody = {
                name: this.name,
                email: this.email,
                description: this.description
            }

            axios.post('http://localhost:8000/api/contact/create', postBody)
            .then((response) => {
                this.alertShow = response.data.success;
                if (response.data.success) {
                    this.name = ''
                    this.email = ''
                    this.description = ''
                }
            })
            .catch((error) => {
                console.log(error);
            });
        },
    }
}
</script>