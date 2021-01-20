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

const wordsnum = {
    cte4:cookie.getCookie('cte4')||'0',
    cte6:cookie.getCookie('cte6')||'0',
    toefl:cookie.getCookie('toefl')||'0',
    ielts:cookie.getCookie('ielts')||'0'
}


const state = {
    userInfo,
    wordsnum
}

export default new Vuex.Store({
    getters,
    state,
    actions,
    mutations
});