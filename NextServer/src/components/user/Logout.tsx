
import { onProps } from '@/modules/types';
import React from 'react';


export default function Logout({props}: any){
    return (
    <form onSubmit={props}>

    <button type = "submit"> 로그아웃 </button> 

    </form>
    )}