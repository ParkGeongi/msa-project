import axios from "axios"
const server = `http://localhost:8000`

export const UserLogin = req => axios.post(`${server}/blog/auth/login`, req)
export const signupApi = req => axios.post(`${server}/auth/signup`, req)