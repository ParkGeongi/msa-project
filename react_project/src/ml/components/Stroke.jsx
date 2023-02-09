
import mlService from 'ml/api';
import { useState } from 'react'

const Stroke =()=>{

    const [inputs, setInputs] = useState({})
    const {id} = inputs;

       const onChange = e =>{
        e.preventDefault()
        const{value,name} = e.target
        setInputs({...inputs, [name]: value})
      }
      
      
    const onClick = e => {
      e.preventDefault()
      
      mlService.stroke(id)
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }
    
    return(<>
      <form method='post'>
      <h1>STROKE</h1>
      <p>번호</p>
      <input type="text" className='box' placeholder=' id ' name = 'id' onChange={onChange}/>
      
    </form>
    <button onClick={onClick}>전송</button>
    </>)
}
export default Stroke
