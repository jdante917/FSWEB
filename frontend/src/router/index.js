import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/index.vue";
import WriteDown from '@/views/writedown'

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path:'/writedown',
        name:'WriteDown',
        component:WriteDown
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;