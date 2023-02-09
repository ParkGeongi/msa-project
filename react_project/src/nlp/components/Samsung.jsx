

import { useState } from 'react'
import 'webcrawler/styles/table.css'
import NLPService from "nlp/api"

const Samsung =()=>{
    const [report, setReport] = useState([])

    



    const onClick = e => {
        e.preventDefault()
        NLPService.getSamsung().then(res => {
          const json = JSON.parse(res)
                    setReport(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0;i<arr.length;i++) arr[i].value = ""
      }
  
      return (<>
        <h2>삼성 리포트</h2>
         
        
        <form method='get'>
          <p>GET?</p>
          <button onClick={onClick}>Click</button>
        </form>
    
        <p>버튼을 클릭하면, 리포트 단어/ 빈도수 출력 </p>
        <table className='type1'>
          <thead>
            <tr>
            <th>순위</th><th>단어</th><th>빈도수</th>
            </tr>
          </thead>
          <tbody>
          {report && report.map(({index,freq_word,freq_num})=>(
    
            <tr key = {index}><td >{index}</td><td>{freq_word}</td><td>{freq_num}</td></tr>
          
          ))}
          </tbody>
        </table>
        </>)
}
export default Samsung