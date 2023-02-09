import { useState } from "react"

const Counter = () => {
    const [count,setCount] = useState(0)
    
    return (<>
    
        <div> 클릭 횟수  : {count} </div>
    
        <button onClick={() => setCount(count+1)}>
            + 버튼</button> 
        <button onClick={() => setCount(count-1)}>
            - 버튼</button> 
    </>)
}

export default Counter