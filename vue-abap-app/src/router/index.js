// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'; // Para Vue 3

// Importa las vistas
import ProductosViews from '../views/ProductosView.vue';
import NuevoProductoViews from '../views/NuevoProductoView.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ProductosViews,
  },
  {
    path: '/nuevoProducto',
    name: 'NuevoProducto',
    component: NuevoProductoViews,
  },
];

const router = createRouter({
  history: createWebHistory(), // Usa el historial HTML5
  routes, // Las rutas definidas
});

export default router;
