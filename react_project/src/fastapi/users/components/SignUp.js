import '../styles/SignUp.css'
import { useState } from "react"
import { useNavigate  } from "react-router-dom"

export default function SignUp() {
    const [inputs, setInputs] = useState({})
    const {user_email, password} = inputs;
    const navigate = useNavigate()

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        
        
    }
    return (<>
        <h2>회원가입</h2>
        <button onClick={onClick}>사용자 등록</button>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
        </>)
}