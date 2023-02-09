import BlogService from "blog/api"
import { useState } from 'react'
const BlogSignup = () =>{

  const [signup, setSignup] = useState()
    

  const onClick = e => {
      e.preventDefault()
      BlogService.getBlogSignup().then(res => {
        const json = JSON.parse(res)
                  setSignup(json['result'])
      })
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }



return (<>
    <h2>회원가입</h2>

      <button onClick={onClick}>사용자 등록</button>
    <p>버튼을 클릭하면,더미 100 명이 등록됩니다.</p>
    <table class='type1'>
      <thead>
        <tr>
        <th>index</th><th>이메일</th><th>패스워드</th><th>닉네임</th>
        </tr>
      </thead>
      <tbody>
      {signup && signup.map(({num,email, nickname, password})=>(

        <tr key = {num}><td>{num}</td><td>{email}</td><td>{password}</td><td>{nickname}</td></tr>
      
      ))}
      </tbody>
    </table>
    </>)


}
export default BlogSignup