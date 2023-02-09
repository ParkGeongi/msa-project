

import DlearnService from 'dlearn/api';
import { useState } from 'react'
import 'webcrawler/styles/table.css'

const Samsung_Stock = () => {
    const [inputs, setInputs] = useState({})

    const {date} = inputs;

    const [stock, setStocks] = useState([])

    const onChange = e =>{
      e.preventDefault()
      const{value,name} = e.target
      setInputs({...inputs, [name]: value})
    }
    
    const GetonClick = e =>{
      e.preventDefault()
      DlearnService.getStock(date)
      .then(res => {
        const json = JSON.parse(res)
          setStocks(json['result'])
      })
      let arr = document.getElementsByClassName('box')
      for(let i = 0;i<arr.length; i++) arr[i].value = ""
    }



    return(<>

    <form method='get'>
      <h1> 삼성 주식 예측</h1>
      <p>날짜 입력해 주세요</p>
      <input type="text" className='box' placeholder='테스트할 날짜/2022-11-11' name = 'date' onChange={onChange}/>
      <button onClick={GetonClick}>GET 전송</button>

    <h2>5일치 데이터를 분석합니다. (주말제외)</h2>
    
    <table class='type2'>
      <thead >
        <tr>
          
        <th>입력 날짜</th><th>예측 날짜</th><th>DNN 예측 종가</th><th>LSTM 예측 종가</th><th>DNN_E예측 종가</th><th>LSTM_E예측 종가</th>
        </tr>
      </thead>
      <tbody>
      {stock && stock.map(({stock_DNN,stock_LSTM,stock_DNN_Ensemble,stock_LSTM_Ensemble,start_day,pred_day})=>(

        <tr key = {start_day}><td>{start_day}</td><td>{pred_day}</td><td>{stock_DNN}</td><td>{stock_LSTM}</td><td>{stock_DNN_Ensemble}</td><td>{stock_LSTM_Ensemble}</td></tr>
      
      ))}
      </tbody>
    </table>
    </form>

    </>)
}

export default Samsung_Stock