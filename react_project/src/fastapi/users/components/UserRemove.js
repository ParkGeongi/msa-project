
import React, { useCallback, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { remove } from 'features/user/reducer/userSlice'
import { useDispatch } from 'react-redux';
import Layout from 'features/common/components/Layout';
import styled from 'styled-components'
export default function UserRemove() {
  const [pwd, setPwd] = useState('')
  const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
  const history = useHistory()
  const dispatch = useDispatch()
  return (
    <Layout><Main>
      <h1>회원탈퇴</h1>
      <form method="DELETE" onSubmit={useCallback(e => {
          e.preventDefault();
          (sessionUser.password === pwd) ? dispatch(remove(sessionUser.userId))
          : document.getElementById('password').value = ''
        })
      }>
    <ul>
        <li>
              <label>
                    <span>사용자아이디 : {sessionUser.username} </span>
                </label>
            </li>
        <li><label htmlFor="pw">비밀번호 확인</label>
        <input type="password" id="password" name="password" onChange={e => {setPwd(e.target.value)}}/></li>
        <li><input type="submit" value="탈퇴요청" /></li>
        <li><input type="button" value="탈퇴취소" onClick={e => history.push("/users/detail")}/></li>
    </ul>
</form>

</Main></Layout>
  );
}

const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`