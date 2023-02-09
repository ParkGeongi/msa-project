

import { useState } from 'react'
import 'webcrawler/styles/table.css'
import NLPService from "nlp/api"

const Review =()=>{
    const [review, setReview] = useState('')
    const [inputs, setInputs] = useState({})


    const onChange = e =>{
        e.preventDefault()
        const{value,name} = e.target
        setInputs({...inputs, [name]: value})
      }
  

      const PostonClick = e => {
        e.preventDefault()
       
        NLPService.postReview(inputs).then(res => {
            const json = JSON.parse(res)
            setReview(json['result'])
          })
        let arr = document.getElementsByClassName('box')
        for(let i=0;i<arr.length;i++) arr[i].value = ""
      }

      return (<>
    <h2>영화 리뷰</h2>
    <p>리뷰 입력</p>
      


    <form method='post'>
    <input type="text" className='box' placeholder=' 리뷰 입력 ' name = 'inputs' onChange={onChange}/>
        <button type="submit" onClick={PostonClick}>post전송</button>
        <p>{review && <a>긍정률 : {(review)} %</a>}</p>
    </form>
        
    
        
        </>)
}
export default Review