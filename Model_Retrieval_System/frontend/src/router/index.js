import Vue from 'vue'
import Router from 'vue-router'
import Index from "../components/Index"
import Homepage from "../components/Homepage"
import All from "../components/All"
import Single from "../components/Single"
import Statistic from "../components/Statistic"
import Utils from "../components/Utils"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      redirect: '/Homepage',
      children: [
        {
          path: '/Homepage',
          name: 'Homepage',
          component: Homepage,
          meta:{
            title:'首页'
          }
        },
        {
          path: '/All',
          name: 'All',
          component: All,
          meta:{
            title:'模型库'
          }
        },
        {
          path: '/Single',
          name: 'Single',
          component: Single,
          meta:{
            title:'单模型检索'
          }
        },
        {
          path: '/Statistic',
          name: 'Statistic',
          component: Statistic,
          meta:{
            title:'模型对比'
          }
        },
        {
          path: '/Utils',
          name: 'Utils',
          component: Utils,
          meta:{
            title:'工具'
          }
        }
      ]
    }
  ]
})

//防止重复点击路由错误
const originalPush = Router.prototype.push
   Router.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
