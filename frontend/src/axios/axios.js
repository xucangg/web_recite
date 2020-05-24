import axios from 'axios'

let host = 'http://127.0.0.1:8080'

export const words = () => {return axios.get(`${host}/wordslength/`)}

export const generate = params => {return axios.get(`${host}/model`, {params:params})}

