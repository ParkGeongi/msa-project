import { useState,useEffect } from "react";
import Pagination from "./admin/Pagination";
import axios from 'axios'

const Home: React.FC = () => {
    const [currentPage, setCurrentPage] = useState(1);
    const lastPage = 3;
    const [list, setList] = useState([])
    const [rowCnt, setRowCnt] = useState(0)
    const [startRowPerPage, setStartRowPerPage] = useState(0)
    const [endRowPerPage, setEndRowPerPage] = useState(0)
    const [startPagePerBlock, setStartPagePerBlock] = useState(0)
    const [endPagePerBlock, setEndPagePerBlock] = useState(0)
    const [requestPage, setRequestPage] = useState(0)
    const [rows, setRows] = useState<number[]>([])
    const [pages, setPages] = useState<number[]>([])
    const [prevArrow,setPrevArrow] = useState(false)
    const [nextArrow,setNextArrow] = useState(false)
    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/14')
        .then(res => {

        const rowCnt = Number(res.data.page_info.row_cnt)
        const startRowPerPage = Number(res.data.page_info.start_row_per_page)
        const endRowPerPage = Number(res.data.page_info.end_row_per_page)
        const startPagePerBlock = Number(res.data.page_info.start_page_per_block)
        const endPagePerBlock = Number(res.data.page_info.end_page_per_block)
        const requestPage = Number(res.data.page_info.request_page)

        const prevArrow = Boolean(res.data.page_info.prev_arrow)
        const nextArrow = Boolean(res.data.page_info.next_arrow)

        const data = res.data.users.items
        setRowCnt(rowCnt)
        setStartRowPerPage(startRowPerPage)
        setEndRowPerPage(endRowPerPage)
        setStartPagePerBlock(startPagePerBlock)
        setEndPagePerBlock(endPagePerBlock)
        setRequestPage(requestPage)
        setPrevArrow(prevArrow)
        setNextArrow(nextArrow)
        setList(data)
        let rows: number[] = []
        let pages: number[] = []
        console.log(' #### 페이지 내용 표시 ###')
        for(let i = startRowPerPage; i <= endRowPerPage; i++){
            rows.push(i)
        }
        setRows(rows)

        console.log(' #### 블록 내용 표시 ###')
        for(let i = startPagePerBlock; i <= endPagePerBlock; i++){
            console.log(i)
            pages.push(i)
        }
        setPages(pages)
        console.log('###요청 페이지 ###')
        console.log(requestPage)
        
    })
        .catch(err => {console.log(err)})
        
    }, [])
    
    return (<>
    <>
    <h2>회원목록 총{rowCnt}명</h2>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>

            { prevArrow && <span> 이전 </span>}
            {list && list.map(({userid, email, password, username, phone, birth, address, job, interests})=>(
                <tr key={userid}>
                    <td>{userid}</td><td>{email}</td><td>{username}</td>
                    <td>{phone}</td><td>{birth}</td><td>{address}</td>
                    <td>{job}</td><td>{interests}</td>
                </tr>
            ))}
            </tbody>
            { nextArrow && <span> 이후 </span>}
        </table>
        </>
         <div>
         {rows && rows.map((idx) => (<span style={{"border": "1px solid black"}}>{(idx)}</span>))}
         </div>
        <div>
          <h3>  
        {pages && pages.map((idx) => (<span style={{"border": "1px solid black"}}>{(idx+1)}</span>))}
        </h3>
        </div>

    </>)
}
export default Home
