import axios from 'axios'

let host = 'http://localhost:8080'

export const words = () => {return axios.get(`${host}/wordslength/`)}

export const wordslist = params => {return axios.get(`${host}/wordslist/`, {params:params})}

export const next = next => {return axios.get(next)}

export const generate = params => {return axios.get(`${host}/model/`, {params:params})}

export const register = parmas => { return axios.post(`${host}/user/`, parmas)}

export const login = params => {return axios.post(`${host}/login/`, params)}

export const useraw = (params,config) => {return axios.post(`${host}/useraw/`, params,config)}

export const wordsdetail = (config) => {return axios.get(`${host}/useraw/`, config)}

export const userinfo = params => {return axios.get(`${host}/userinfo/`, params)}

export const userlearned = (params,config) => {return axios.post(`${host}/userlearned/`, params,config)}

export const learnedDetail= (config) => {return axios.get(`${host}/userlearned`, config)}

export const usercurlearned = (config) => {return axios.get(`${host}/usercurlearned`, config)}