import {useState,useEffect} from 'react'
import axios from 'axios'
import NameForm from 'security/components/NameForm'

export default function Name(){
    const [list,setList] = useState([])

    

    useEffect(()=>{
    
        axios
        .get('http://localhost:8000/security/list/name')
        .then(res => {
            setList(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])


    return <>
        <NameForm list={list}/>
    </>
}
