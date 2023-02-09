import { Route, Routes } from "react-router-dom"
import {Navigation, Footer} from "admin"
import { Schedule } from "todos"
import {Login,SignUp,UserList} from "fastapi"


const Home = () => {
    return (<>
    <table style={{ width: "1200px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead style={{ height: "20%",  border: "1px solid black"}}>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "70%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>

                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/login" element={<Login/>}></Route>
                <Route path="/signup" element={<SignUp/>}></Route>
                <Route path="/user-list" element={<UserList/>}></Route>
            </Routes>
            </td>
        </tr>
        
        <tr style={{ width: "100%", height: "10%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
export default Home