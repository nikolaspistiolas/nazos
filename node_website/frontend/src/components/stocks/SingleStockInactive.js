import React from 'react';
import axios from "axios";




function SingleStockInactive(props){
    let a = null;
    function activateSymbol(props){
        const body = {symbol: a, active: true}
        axios.patch('/stocks',body)
        window.location.reload(false);
    }
    return(
        <div>
            <button  className="activate-button" onClick={activateSymbol}>{a = props.symbol}</button>
        </div>
    )

}

export default SingleStockInactive;