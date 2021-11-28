import React from 'react';
import SingleStockActive from "./SingleStockActive";
import axios from 'axios';

function ActiveStocksList(props) {
    return (
        <ul className="button-container">
            {props.stocks.map((stock)=> (
                <SingleStockActive
                    symbol={stock.symbol}
                />
            ))}
        </ul>
    )

}

export default ActiveStocksList;