import 'todos/styles/TodoList.css'
import { useSelector } from 'react-redux'
import { Naver } from 'webcrawler'

const NaverList = () => {
    const navers = useSelector((state) => state.navers)
    return (<>
    <ul>
        {navers.map( naver => (
            <Naver key={naver.id} id={naver.id} text={naver.text} />
        ))} 
    </ul>
    </>)
}
export default NaverList