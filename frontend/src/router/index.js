import Vue from 'vue'
import Router from 'vue-router'
import home from '@/page/home.vue'
import model from '@/page/model.vue'
import recite from '@/page/recite.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name:'home',
      component: home,
    },
    {
      path:'/model',
      name:'model',
      component: model,
    },
    {
      path:'/recite',
      name:'recite',
      component: recite,
    },
  ]
})
