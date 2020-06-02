import axios from 'axios'

let host = 'http://127.0.0.1:8080'

export const words = () => {return axios.get(`${host}/wordslength/`)}

export const wordslist = params => {return axios.get(`${host}/wordslist/`, {params:params})}

export const generate = params => {return axios.get(`${host}/model/`, {params:params})}

export const register = parmas => { return axios.post(`${host}/user/`, parmas)}

export const login = params => {return axios.post(`${host}/login/`, params)}

