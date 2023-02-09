import 'auth/styles/SignUp.css'

import { useState } from 'react'
import{ signupApi } from '../api'




const SignUp = () =>{
    
  const [inputs, setInputs] = useState({})
  const {email, password, nickname} = inputs;
  
  const onChange = e =>{
    e.preventDefault()
    const{value,name} = e.target
    setInputs({...inputs, [name]: value})
  }
  
  const onClick = e =>{
    e.preventDefault()
    const signupRequest = {email, password, nickname}
    alert(`사용자 이름 : ${JSON.stringify(signupRequest)}`)
    signupApi(signupRequest)
    .then((res)=>{
      console.log(`Response is ${res}`)
      localStorage.setItem('token', JSON.stringify(res.config.data)) // 임시 저장소 response 저장해놈

    }) //success reponse는 내가 보낸 requset한거에 추가로 뭔가 있다 추가한게 장고가 보낸거라고 알고 있다
    .catch((err)=>{
      console.log(err)
      alert('이메일와 비밀번호 다시 입력해주세요')
    }) //fail
    
  }
    
    
    return (<>
    
    <form action="action_page.php" style={{border:"1px solid #ccc"}}>
  <div className="container">
    <h1>Sign Up</h1>
    <div>Please fill in this form to create an account.</div>
    <hr></hr>

    <label htmlFor="text"><b>Email</b></label>
    <input type="text" placeholder="Enter email" name="email"  onChange={onChange} required/>

    <label htmlFor="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password"  onChange={onChange} required/>

    <label htmlFor="nickname"><b>Nickname</b></label>
    <input type="text" placeholder="nickname" name="nickname"  onChange={onChange} required/>

    <label>
      <input type="checkbox"  name="remember" style={{marginbottom:"15px"}}/> Remember me
    </label>

    <div>By creating an account you agree to our <a  href="home" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</div>

    <div className="clearfix">
      <br/>
      <button onClick={onClick}  className="signupbtn">Sign Up</button>
    </div>
  </div>
</form>

    </>)
}

export default SignUp