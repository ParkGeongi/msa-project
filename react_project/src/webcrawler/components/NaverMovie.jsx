import WebcrawlerService from "webcrawler/api"
import { useState } from 'react'
import 'webcrawler/styles/table.css'

const NaverMovie =()=>{
    const [movie, setMovie] = useState()

    const onClick = e => {
        e.preventDefault()
        WebcrawlerService.getNaver().then(res => {
          const json = JSON.parse(res)
                      setMovie(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0;i<arr.length;i++) arr[i].value = ""
      }
  
    return (<>
    <h2>네이버 영화 크롤링</h2>
     
    
    <form method='get'>
      <p>가져올래?</p>
      <button onClick={onClick}>전송</button>
    </form>

    <p>버튼을 클릭하면, 네이버 영화 목록이 출력됩니다.</p>
    <table className='type1'>
      <thead>
        <tr>
        <th>순위</th><th>영화목록</th>
        </tr>
      </thead>
      <tbody>
      {movie && movie.map(({rank,title})=>(

        <tr key = {rank}><td>{rank}</td><td>{title}</td></tr>
      
      ))}
      </tbody>
    </table>
    </>)
}
export default NaverMovie