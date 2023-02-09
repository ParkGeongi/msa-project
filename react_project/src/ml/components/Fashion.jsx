
import mlService from 'ml/api';
import { useState } from 'react'


const Fashion = () => {
    const [inputs, setInputs] = useState({})

    const {id} = inputs;

    
    const onChange = e =>{
      e.preventDefault()
      const{value,name} = e.target
      setInputs({...inputs, [name]: value})
    }


    const onClick = e => {
      e.preventDefault()
      
      mlService.getFashion(id)
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }

    const onClick2 = e =>{
      e.preventDefault()
      
      mlService.postFashion(id)
      let arr = document.getElementsByClassName('box')
      for(let i = 0;i<arr.length; i++) arr[i].value = ""
    }

    return(<>
    <form method='get'>
      <h1>FASHION GET</h1>
      <p>카테코리를 알고 싶은 옷의 번호를 입력해 주세요</p>
      <input type="text" className='box' placeholder='테스트할 옷 번호 ' name = 'id' onChange={onChange}/>
      <button onClick={onClick}>GET 전송</button>
    </form>
    <form method='post'>
      <h1>FASHION POST</h1>
      <p>카테코리를 알고 싶은 옷의 번호를 입력해 주세요</p>
      <input type="text" className='box' placeholder='테스트할 옷 번호 ' name = 'id' onChange={onChange}/>
      <button onClick={onClick2}>POST 전송</button>
    </form>
    </>)
}

export default Fashion