import { SET_INFO,SET_USER_SAVE_WORDS,SET_WORDS_NUM } from './mutation-types'
import cookie from '../static/js/cookie';

export default {
    [SET_INFO] (state) {
        state.userInfo = {
            name:cookie.getCookie('name'),
            token:cookie.getCookie('token')
        }
    },
    [SET_USER_SAVE_WORDS] (state){
        if(cookie.getCookie('token') != null){
            state
        }
    },
    [SET_WORDS_NUM] (state){
        state.wordsnum = {
            cte4:cookie.getCookie('cte4'),
            cte6:cookie.getCookie('cte6'),
            toefl:cookie.getCookie('toefl'),
            ielts:cookie.getCookie('ielts')
        }
    }
}