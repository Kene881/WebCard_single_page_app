import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import './index.css'
import axios from 'axios';


axios.defaults.withCredentials = true;

createApp(App).use(store).mount('#app')
