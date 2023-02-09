import { nlp,server } from "context";

const NLPService = {
    getSamsung,getReview,postReview
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

    async function postReview(req){
        const requestOption = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(req)
        }
        const res = await fetch(`${server}${nlp}review`, requestOption)
        .then(handleResponse)
        .then(data => JSON.stringify(data))
        .catch((error) => {
            alert('error :::: '+error)
        })
        return Promise.resolve(res) 
    }

    async function getReview(req2){
        const res = await fetch(`${server}${nlp}review?req2=${req2}`)
        .then(handleResponse)
        .then(data =>  JSON.stringify(data))
        .catch((error) => {
            alert('error ::::'+error)
        })
         return Promise.resolve(res);          
        }

async function getSamsung(){
    const res = await fetch(`${server}${nlp}samsung-report`)
    .then(handleResponse)
    .then(data =>  JSON.stringify(data))
    .catch((error) => {
        alert('error ::::'+error)
    })
     return Promise.resolve(res);          
    }

export default NLPService