import React from 'react';
import ActiveStocks from "./ActiveStocks";
import InactiveStocks from "./InactiveStocks";
import InputStock from "./InputStock";


function AllStocks(){
    return(

        <div className='Stockparent'>
            <div className="input" >
                <InputStock />
            </div>
            <div className="element">
                <ActiveStocks />
            </div>
            <div className="element">
                <InactiveStocks />
            </div>
        </div>
    )
}

export default AllStocks;