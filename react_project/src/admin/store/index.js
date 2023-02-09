import { configureStore,
    combineReducers // redux의 Reducer 의 집합과 같다.
} from '@reduxjs/toolkit';

import users from "fastapi/users/reducers/userSlice"
import todos from "todos/reducers/todo.reducer"


const rootReducer = combineReducers({ todos, users })
export const store = configureStore({
    reducer: rootReducer
  })