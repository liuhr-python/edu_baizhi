// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'


// axios配置
import axios from "axios";

Vue.prototype.$axios = axios;

//element-ui
import Element from "element-ui"
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element);

// 全局css
import "../static/css/global.css"

// 自定义域名
import settings from "./settings";

Vue.prototype.$settings = settings;
Vue.config.productionTip = false

// 导入极验
import "../static/js/gt.js"

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: {App},
    template: '<App/>'
})
