// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
 import Vue from 'vue'
 import App from './App'
 import router from './router'
 import ElementUi from 'element-ui'
 import 'element-ui/lib/theme-chalk/index.css'
 import {Dropdown, DropdownMenu} from 'element-ui'
 import store from './store/store'

Vue.use(ElementUi,Dropdown,DropdownMenu);

/* eslint-disable no-new */
 new Vue({
  el: '#app',
  render: h => h(App),
  components: { App },
  router,
  store,
  template: '<App/>'
})

