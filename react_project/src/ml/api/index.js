
import { ml, server } from "context";

const mlService = {
   stroke, getIris, postIris, getFashion, postFashion , postNumber,getNumber
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

async function stroke(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}${ml}stroke`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert(JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}



async function postIris(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}${ml}iris`, requestOption)
    .then(handleResponse)
    .then(data => {
        console.log(`POST Response is ${data.result}`)
        alert(JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function getIris(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm){
    fetch(`${server}${ml}iris?SepalLengthCm=${SepalLengthCm}&SepalWidthCm=${SepalWidthCm}&PetalLengthCm=${PetalLengthCm}&PetalWidthCm=${PetalWidthCm}`)
    .then(handleResponse)
    .then(data => {
        console.log(`GET Response is ${data.result}`)
        alert('결과: '+JSON.stringify(data))
    })
} 

async function postFashion(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}${ml}fashion`, requestOption)
    .then(handleResponse)
    .then(data => {
        console.log(`POST Response is ${data.result}`)
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function getFashion(id){
    fetch(`${server}${ml}fashion?id=${id}`)
    .then(handleResponse)
    .then(data => {
        console.log(`GET Response is ${data.result}`)
        alert('결과: '+JSON.stringify(data))
    })
} 
async function postNumber(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}${ml}number`, requestOption)
    .then(handleResponse)
    .then(data => {
        console.log(`POST Response is ${data.result}`)
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function getNumber(id){
    fetch(`${server}${ml}number?id=${id}`)
    .then(handleResponse)
    .then(data => {
        console.log(`GET Response is ${data.result}`)
        alert('결과: '+JSON.stringify(data))
    })
} 
export default mlService