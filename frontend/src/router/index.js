import Vue from 'vue'
import Router from 'vue-router'
import home from '@/page/home.vue'
import model from '@/page/model.vue'
import recite from '@/page/recite.vue'
import register from '@/page/register.vue'
import login from '@/page/login.vue'
import vocabulary from '@/page/vocabulary.vue'
import personal from '@/page/personal.vue'
import no_resource from '@/components/no_resource.vue'
import review from '@/page/review.vue'


Vue.use(Router)

export default new Router({
  mode:'history',
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
    },
    {
      path:'/personal',
      name:'personal',
      component: personal,
    },
    {
      path:'/reviewWords',
      name:'reviewWords',
      component: review,
    },
    {
      path:'*',
      component: no_resource,
    }
  ]
})
