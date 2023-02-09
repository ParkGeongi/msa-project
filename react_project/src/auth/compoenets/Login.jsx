import 'auth/styles/Login.css'
import { useState } from 'react'
import{ UserLogin } from '../api'

const Login = () => {
  const [inputs, setInputs] = useState({})
  const {email, password} = inputs;
  
  const onChange = e =>{
    e.preventDefault()
    const{value,name} = e.target
    setInputs({...inputs, [name]: value})
  }
  
  const onClick = e =>{
    e.preventDefault()
    const loginRequest = {email, password}
    alert(`사용자 이름 : ${JSON.stringify(loginRequest)}`)
    UserLogin(loginRequest)
    .then((res)=>{
      console.log(`Response is ${res.config.data}`)
      localStorage.setItem('token', JSON.stringify(res.config.data)) // 임시 저장소 response 저장해놈

    }) //success reponse는 내가 보낸 requset한거에 추가로 뭔가 있다 추가한게 장고가 보낸거라고 알고 있다
    .catch((err)=>{
      console.log(err)
      alert('이메일와 비밀번호 다시 입력해주세요')
    }) //fail   
  }
  


  return(<>
    <h2>Login Form</h2>

  <form action="auth/action_page.php" method="post">
  <div className="imgcontainer">
  <img src="https://www.w3schools.com/howto/img_avatar2.png" alt="Avatar" className="avatar" ></img>
  </div>

  <div className="container">
    <label htmlFor="uname"><b>Email</b></label>
    <input type="text" placeholder="Enter email" name="email"  onChange={onChange} required/>

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

export default Login