import { useState } from "react"
import 'auth/styles/Login.css'

export default function NameForm({list}){
    const [inputs, setInputs] = useState({})
    const username = inputs
    const onChange = e =>{
        e.preventDefault()
        const{value,name} = e.target
        setInputs({...inputs, [name]: value})
      }
  
    const onClick = e => {
        e.preventDefault()
        const request = {username}  
        let arr = document.getElementsByClassName('box')
        for(let i=0;i<arr.length;i++) arr[i].value = ""
      }
  
    return <>
    <h2>회원목록</h2>
    <input type="text" className='box' placeholder='이름 입력 창' name = 'username' onChange={onChange}/>
    <button onClick={onClick}>버튼</button>
        
        <table class='type2'>
        <thead>
        <tr>
        <th>번호</th><th>이메일</th><th>패스워드</th><th>이름</th><th>전화번호</th><th>생일</th><th>사는 곳</th><th>직업</th><th>취미</th>
        </tr>
        </thead>
        <tbody>
        {list && list.map(({susers_id,user_email,password, user_name, phone,birth,address,job,user_interests})=>(

        <tr key = {susers_id}><td>{susers_id}</td><td>{user_email}</td><td>{password}</td><td>{user_name}</td><td>{phone}</td><td>{birth}</td><td>{address}</td><td>{job}</td><td>{user_interests}</td></tr>

        ))}
        </tbody>
        </table>
    </>
}