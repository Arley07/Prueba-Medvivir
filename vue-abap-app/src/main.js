// src/main.js

import { createApp } from 'vue'; // Para Vue 3
import App from './App.vue';
import router from './router'; // Importa el enrutador

createApp(App).use(router).mount('#app');
