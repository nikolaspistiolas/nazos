import React from 'react';
import axios from 'axios';



function SingleStockActive(props){
    let a = null;
    function deactivateSymbol(props){
        console.log(a);
        const body = {symbol: a, active: false}
        const ret = axios.patch('/stocks',body)
        console.log(ret)
        window.location.reload(false);
    }
    return(
        <div>
            <button  className="deactivate-button" onClick={deactivateSymbol}>{a = props.symbol}</button>
        </div>
    )

}

export default SingleStockActive;