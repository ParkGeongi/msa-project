
import axios from "axios";
import { security, server } from "context";

export const postLogin = req => axios.post(`${server}${security}seq-login`, req)


const SecurityService = {
    getSuserSignup
}

function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }




async function getSuserSignup(){
    const res = await fetch(`${server}${security}sequser`)
    .then(handleResponse)
    .then(data =>  JSON.stringify(data))
    .catch((error) => {
        alert('error ::::'+error)
    })
     return Promise.resolve(res);          
    }

export default SecurityService