
import mlService from 'ml/api';
import { useState } from 'react'


const Number = () => {
    const [inputs, setInputs] = useState({})

    const {id} = inputs;

    
    const onChange = e =>{
      e.preventDefault()
      const{value,name} = e.target
      setInputs({...inputs, [name]: value})
    }


    const PostonClick = e => {
      e.preventDefault()
      
      mlService.postNumber(id)
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }
    
    const GetonClick = e =>{
      e.preventDefault()
      mlService.getNumber(id)
      let arr = document.getElementsByClassName('box')
      for(let i = 0;i<arr.length; i++) arr[i].value = ""
    }

    return(<>
    <form method='post'>
      <h1>Number Mnist POST</h1>
      <p>인덱스 번호를 입력해 주세요</p>
      <input type="text" className='box' placeholder='테스트할 번호 ' name = 'id' onChange={onChange}/>
      <button onClick={PostonClick}>POST 전송</button>
    </form>
    <form method='get'>
      <h1>Number Mnist GET</h1>
      <p>인덱스 번호를 입력해 주세요</p>
      <input type="text" className='box' placeholder='테스트할 번호 ' name = 'id' onChange={onChange}/>
      <button onClick={GetonClick}>GET 전송</button>
    </form>
    
    </>)
}

export default Number