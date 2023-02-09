
import { blog, server } from "context";

const BlogService = {
   getBlogSignup
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



async function getBlogSignup(){
    const res = await fetch(`${server}${blog}blog-signup`)
    .then(handleResponse)
    .then(data =>  JSON.stringify(data))
    .catch((error) => {
        alert('error ::::'+error)
    })
     return Promise.resolve(res);          
    }

export default BlogService