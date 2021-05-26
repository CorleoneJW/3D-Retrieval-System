// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import * as echarts from 'echarts';
import '@/assets/theme/index.css';
import axios from 'axios'

Vue.use(ElementUI)
Vue.use(VueResource)
Vue.use(axios)
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  components: { App },
  template: '<App/>'
})

/* router中meta修改title */
router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})
