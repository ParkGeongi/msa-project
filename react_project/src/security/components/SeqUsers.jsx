
import { useState } from 'react'
import SecurityService from 'security/api'
import 'security/styles/table.css'
const SeqUsers = () =>{

  const [user, setUsers] = useState()
    

  const onClick = e => {
      e.preventDefault()
      SecurityService.getSuserSignup().then(res => {
        const json = JSON.parse(res)
                setUsers(json['result'])
      })
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }



return (<>
    <h2>회원가입</h2>

      <p></p>
      <button onClick={onClick}>사용자 등록</button>
    <p>버튼을 클릭하면,더미 100 명이 등록됩니다.</p>
    <table class='type2'>
      <thead >
        <tr>
        <th>이메일</th><th>패스워드</th><th>이름</th><th>전화번호</th><th>생일</th><th>사는 곳</th><th>직업</th><th>취미</th>
        </tr>
      </thead>
      <tbody>
      {user && user.map(({user_email,password, user_name, phone,birth,address,job,user_interests})=>(

        <tr key = {user_email}><td>{user_email}</td><td>{password}</td><td>{user_name}</td><td>{phone}</td><td>{birth}</td><td>{address}</td><td>{job}</td><td>{user_interests}</td></tr>
      
      ))}
      </tbody>
    </table>
    </>)


}
export default SeqUsers