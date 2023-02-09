import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import userAPI from './userAPI';

const JOIN = async (x) => {
   const res = await userAPI.join(x)
   return res.data
}
const EXIST = async (x) => {
  const res = await userAPI.exist(x)
  return res.data
}
const DETAIL = async (x) => {
  const res = await userAPI.detail(x)
  return res.data
}
const LIST = async ({page}) => {
  const res = await userAPI.list(page)
  return res.data
}
const LOGIN = async (x) => {
  const res = await userAPI.login(x) 
  return res.data
}
const MODIFY = async (x) => {
  const res = await userAPI.modify(x)
  return res.data
}
const REMOVE = async (x) => {
  const res = await userAPI.remove(x)
  return res.data
}

export const join = createAsyncThunk('users/join', JOIN)
export const exist = createAsyncThunk('users/exist', EXIST)
export const detail = createAsyncThunk('users/dtail', DETAIL)
export const list = createAsyncThunk('users/list', LIST)
export const login = createAsyncThunk('users/login', LOGIN)
export const modify = createAsyncThunk('users/modify', MODIFY)
export const remove = createAsyncThunk('users/remove', REMOVE)

const changeNull = ls =>{
  for(const i of ls ){
    document.getElementById(i).value = ''
  }
}
const userSlice = createSlice({
  name: 'users',
  initialState: {
    userState: {username:'', password:'', email:'', name:'', regDate: ''},
    usersState: [],
    type: '',
    keyword: '',
    params: {}
  },
  
  reducers: {},
  extraReducers: {
    [join.fulfilled]: ( state, action ) => { 
      state.userState = action.payload 
      window.location.href = `/users/login`
    },
    [exist.fulfilled]: ( state, action ) => { 
      if(action.payload){window.location.href='/users/add'}
      else{ alert(`사용가능함`) }
    },
    [detail.fulfilled]: ( state, {meta, payload} ) => { state.userState = payload},
    [list.fulfilled]: ( state, {meta, payload} ) => { 
      state.usersState = payload },
    [login.fulfilled]: ( state, {meta, payload} ) => {
      state.userState = payload
      window.localStorage.setItem('sessionUser', JSON.stringify(payload))
      if(payload.username != null){
        alert(`${payload.name}님 환영합니다`)
        window.location.href = `/users/detail`
      }else{
        alert('아이디, 비번 오류로 로그인 실패  ')
        changeNull(['username','password'])
      }
    },
    [modify.fulfilled]: ( state, action ) => { 
      localStorage.setItem('sessionUser', JSON.stringify(action.payload))
      window.location.href = "/users/detail"
    },
    [remove.fulfilled]: () => { 
      window.localStorage.removeItem("sessionUser"); 
      window.localStorage.clear(); 
      window.location.href = "/home"
    }
  }

})
export const currentUserState = state => state.users.userState
export const currentUsersState = state => state.users.usersState
export const currentUserParam = state => state.users.param
export default userSlice.reducer;