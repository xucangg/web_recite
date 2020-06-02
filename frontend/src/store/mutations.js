import { SET_INFO,SET_USER_SAVE_WORDS } from './mutation-types'
import cookie from '../static/js/cookie';

export default {
    [SET_INFO] (state) {
        state.userInfo = {
            name:cookie.getCookie('name'),
            token:cookie.getCookie('token')
        }
        console.log(state.userInfo);
    },
    [SET_USER_SAVE_WORDS] (state){
        if(cookie.getCookie('token') != null){
            state
        }
    }
}