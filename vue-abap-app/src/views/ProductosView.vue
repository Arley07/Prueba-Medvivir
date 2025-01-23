<script>
import axios from "axios";
import {ref, onMounted} from "vue";

export default {
    setup() {

        onMounted(()=>{
            listarProdcutos();
        })

        const productos = ref([]);

        const listarProdcutos = async()=>{
            try{

                const response = await axios.get("http://localhost:3000/productos");
                productos.value = response.data;
                console.log(productos.value);

            } catch (error){

                console.log("Error al leer los productos desde el endpoint", error);

            }

            return{
                productos,
            };
        }
    }
}
</script>
<template>
    <main>
        <table>
            <thead>
                <tr>
                    <th>id</th>
                    <th>Producto</th>
                    <th>Autor</th>
                    <th>Precio</th>
                    <th>Genero</th>
                    <th>Disponibilidad</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="producto in productos" :key="producto.id">
                    <td>{{ producto.id }}</td>
                    <td>{{ producto.producto }}</td>
                    <td>{{ producto.autor }}</td>
                    <td>{{ producto.precio }}</td>
                    <td>{{ producto.genero }}</td>
                    <td>{{ producto.disponibilidad }}</td>
                    <td>{{ producto.acciones }}</td>
                </tr>
            </tbody>
        </table>
    </main>
</template>
<style>
</style>