import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/icons/iconfont.css'
// import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css';
import { Button, Menu,DatePicker  } from 'ant-design-vue'
import bus from './eventBus'
import * as echarts from 'echarts'


const app = createApp(App)
app.config.globalProperties.$echarts=echarts
app.config.globalProperties.$bus = bus
app.use(router).use(Button).use(Menu).use(DatePicker).mount('#app')
