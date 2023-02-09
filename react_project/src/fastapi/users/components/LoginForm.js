import '../styles/Login.css'
import { useDispatch } from 'react-redux';
import login from '../reducers/userAPI'
import { useForm } from "react-hook-form";
import styled from 'styled-components'
import { Layout, Header, Footer } from 'admin';

export default function LoginForm(){
    const dispatch = useDispatch()
    const { register, handleSubmit, formState: { errors } } = useForm();

    return (
        <Layout><Main>
        <h1>로그인</h1>
            <form method='POST' 
            onSubmit={ 
                handleSubmit(async (data) => {await dispatch(login(data))})}>
                <ul>
                    <li>
                        <label>아이디 : </label>
                        <input type="text" id="username" 
                            {...register('username', { required: true, maxLength: 30 })}
                            size="10" minlength="4" maxlength="15"/>
                            {errors.username && errors.username.type === "required" && (
                                <Span role="alert">아이디는 필수값입니다</Span>
                            )}
                            {errors.username && errors.username.type === "maxLength" && (
                                <Span role="alert">아이디는 4자에서 15 글자이어야 합니다.</Span>
                            )}
                        <br/>
                        <small>4~15자리 이내의 영문과 숫자</small>
                    </li>
                    <li>
                        <label>비밀 번호 : </label>
                        <input type="password" id="password" 
                            aria-invalid={errors.name ? "true" : "false"}
                            {...register('password', { required: true, maxLength: 30 })}
                            size="10" minlength="1" maxlength="15"/>
                        {errors.password && errors.password.type === "required" && (
                            <Span role="alert">비밀 번호는 필수값입니다</Span>
                        )}
                        {errors.password && errors.password.type === "maxLength" && (
                            <Span role="alert">비밀 번호는 1자에서 15 글자이어야 합니다.</Span>
                        )}
                    </li>
                </ul>
                <input type="submit" value="로그인"/> 
                </form>
                </Main>
            </Layout>
 );
}
const Span = styled.span`
   color: red
`
const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`