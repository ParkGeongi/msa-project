import axios from 'axios';
const SERVER = 'http://localhost:8000' 
const headers = {
  'Content-Type' : 'application/json',
  'Authorization': 'JWT fefege..'
}

const join = x => axios.post(`${SERVER}/users`, JSON.stringify(x),{headers})
const exist = x => axios.get(`${SERVER}/users/exist/${x}`)
const detail = x => axios.get(`${SERVER}/users/${x.userId}`)
const list = x => axios.get(`${SERVER}/users/list/${x}`)
const login = x => axios.post(`${SERVER}/users/login`, JSON.stringify(x),{headers})
const modify = x => axios.put(`${SERVER}/users`, JSON.stringify(x),{headers})
const remove = x => axios.delete(`${SERVER}/users/${x}`,JSON.stringify(x),{headers})

export default {
  join,
  exist,
  detail,
  list,
  login,
  modify,
  remove
} 