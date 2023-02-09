import {useState,useEffect} from 'react'
import axios from 'axios'
import SeqUserListForm from 'security/components/SeqUserListForm'

export default function SeqUserList(){
    const [list,setList] = useState([])

    

    useEffect(()=>{
    
        axios
        .get('http://localhost:8000/security/list')
        .then(res => {
            setList(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])


    return <>
        <SeqUserListForm list={list}/>
    </>
}
