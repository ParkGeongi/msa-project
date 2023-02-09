import { createSlice } from "@reduxjs/toolkit"
import { v4 as uuidv4 } from 'uuid'

const naverSlice = createSlice({
  name: 'navers',
  initialState: [],
  reducers : {
    addNaver(state, action) {
      const newNaver = {
        id: uuidv4(),
        text: action.payload.text
      }
      state.push(newNaver)
    }, 
    deleteNaver(state, action) {
      return state.filter((naver) => naver.naver !== action.payload.id)
    }
  }
})

export const { addNaver, deleteNaver } = naverSlice.actions

export default naverSlice.reducer