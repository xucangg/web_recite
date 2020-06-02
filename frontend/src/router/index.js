import Vue from 'vue'
import Router from 'vue-router'
import home from '@/page/home.vue'
import model from '@/page/model.vue'
import recite from '@/page/recite.vue'
import register from '@/page/register.vue'
import login from '@/page/login.vue'
import vocabulary from '@/page/vocabulary.vue'
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
    {
      path:'/register',
      name:'register',
      component: register,
    },
    {
      path:'/login',
      name:'login',
      component: login,
    },
    {
      path:'/vocabulary',
      name:'vocabulary',
      component: vocabulary,
    }
  ]
})
