import 'auth/styles/Login.css'
import { useState } from 'react'

import { postLogin } from 'security/api';
import {useNavigate} from "react-router-dom";


export default function LoginForm(){
  const [inputs, setInputs] = useState({})
  const {user_email, password} = inputs;
  const navigate = useNavigate()

  const onChange = e =>{
    e.preventDefault()
    const{value,name} = e.target
    setInputs({...inputs, [name]: value})
  }
  
  const onClick = e =>{
    e.preventDefault()
    const request = {user_email, password}
    alert(`사용자 이름 : ${JSON.stringify(request)}`)
    postLogin(request)
    .then((res)=>{
      alert(`Response is ${JSON.stringify(res.data)}`)
      localStorage.setItem("loginSeqUser",JSON.stringify(res.data))
      navigate("/")
    })
    .catch((err)=>{
      console.log(err)
      alert('아이디와 비밀번호를 다시')
    })

    let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
  
  }
  


  return(<>
    <h2>Login Form</h2>

  <form action="auth/action_page.php" method="post">
  <div className="imgcontainer">
  <img src="https://www.w3schools.com/howto/img_avatar2.png" alt="Avatar" className="avatar" ></img>
  </div>

  <div className="container">
    <label htmlFor="uname"><b>Email</b></label>
    <input type="text" placeholder="Enter email" name="user_email"  onChange={onChange} required/>

    <label htmlFor="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password"  onChange={onChange} required/>
    <input type="checkbox" name="remember"/> Remember me<br/>
    <br/>
    
    <button onClick={onClick}  className="Loginbtn">Login</button>
    
    
  </div>
    
 
    
    <span className="psw"><a href="home"> Forgot password?</a></span>
  
</form>


    </>)
}

