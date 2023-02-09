import { ChangeEvent,FormEvent, useState } from "react"
import { NextPage } from "next"
import { Login,  GoogleLogin} from "@/components/user"
import { User } from "@/modules/types"
import { useDispatch } from "react-redux"
import { loginRequest } from "@/modules/slices"
import {useAppDispatch, useAppSelector} from '@/hooks'
import { UserLoginInput } from "@/modules/types"

const LoginPage: NextPage = function(){
    const [loginInfo, setLoginInfo] = useState<UserLoginInput>({email:'', password:''})
    const dispatch = useDispatch()

    const onChange = (e: ChangeEvent<HTMLInputElement>) => {
        e.preventDefault()
        const { name, value} = e.currentTarget
        setLoginInfo({...loginInfo, [name]:value})
    }
    const onSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        
        dispatch(loginRequest(loginInfo))
    }
    return (
        <>
           <Login onChange={onChange} onSubmit={onSubmit}/>
           <GoogleLogin onChange={onChange} onSubmit={onSubmit}/>
        </>
            
        
 );
}
LoginPage.getInitialProps =async (ctx) => {
    const pathname = ctx.pathname
    return { pathname }
}
export default LoginPage