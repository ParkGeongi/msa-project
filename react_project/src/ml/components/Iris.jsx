
import mlService from 'ml/api';
import { useState } from 'react'


const Iris = () => {
    const [inputs, setInputs] = useState({})
    const {SepalLengthCm, SepalWidthCm,PetalLengthCm,PetalWidthCm} = inputs;
    
    const onChange = e =>{
      e.preventDefault()
      const{value,name} = e.target
      setInputs({...inputs, [name]: value})
    }
    
    const onClick = e => {
      e.preventDefault()
      const request = {SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm}
      mlService.postIris(request)
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }
    const onClick2 = e => {
      e.preventDefault()
      mlService.getIris(SepalLengthCm, SepalWidthCm,PetalLengthCm,PetalWidthCm)
      let arr = document.getElementsByClassName('box')
      for(let i=0;i<arr.length;i++) arr[i].value = ""
    }

    return(<>
    <form method='post'>
      <h1>IRIS POST</h1>
      <p>꽃잎 폭</p>
      <input type="text" className='box' placeholder='SepalLengthCm ' name = 'SepalLengthCm' onChange={onChange}/>
      <p>꽃잎 길이</p>
      <input type="text" className='box' placeholder='SepalWidthCm ' name = 'SepalWidthCm' onChange={onChange}/>
      <p>꽃받침 폭</p>
      <input type="text" className='box' placeholder='PetalLengthCm ' name = 'PetalLengthCm' onChange={onChange}/>
      <p>꽃받침 길이</p>
      <input type="text" className='box' placeholder='PetalWidthCm ' name = 'PetalWidthCm' onChange={onChange}/>
      <button onClick={onClick}>POST 전송</button>
    </form>
    <form method='get'>
      <h1>IRIS GET</h1>
      <p>꽃잎 폭</p>
      <input type="text" className='box' placeholder='SepalLengthCm ' name = 'SepalLengthCm' onChange={onChange}/>
      <p>꽃잎 길이</p>
      <input type="text" className='box' placeholder='SepalWidthCm ' name = 'SepalWidthCm' onChange={onChange}/>
      <p>꽃받침 폭</p>
      <input type="text" className='box' placeholder='PetalLengthCm ' name = 'PetalLengthCm' onChange={onChange}/>
      <p>꽃받침 길이</p>
      <input type="text" className='box' placeholder='PetalWidthCm ' name = 'PetalWidthCm' onChange={onChange}/>
      <button onClick={onClick2}>GET 전송</button>
    </form>
    </>)
}

export default Iris