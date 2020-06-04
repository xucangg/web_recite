import * as getters from './getters'
import * as actions from './actions'
import mutations from './mutations'


import Vue from 'vue'
import Vuex from 'vuex';
import cookie from '../static/js/cookie'

Vue.use(Vuex)

const userInfo = {
    name:cookie.getCookie('name')||'',
    token:cookie.getCookie('token')||''
}


const state = {
    userInfo,
}

export default new Vuex.Store({
    getters,
    state,
    actions,
    mutations
});