import { NextPage } from "next"

import Counter from "@/components/counter/counter"
import { Provider } from "react-redux"
import store from "@/modules/store"
import { any } from "prop-types"


const CounterPage: NextPage = function(){
    return (<>

            <Counter />

    </>)
} 
export default  CounterPage