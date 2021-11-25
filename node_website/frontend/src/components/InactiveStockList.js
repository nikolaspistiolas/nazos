import React from 'react';
import SingleStockInactive from "./SingleStockInactive";
import axios from 'axios';

function InactiveStocksList(props) {
    return (
        <ul className="button-container">
            {props.stocks.map((stock)=> (
                <SingleStockInactive
                    symbol={stock.symbol}
                />
            ))}
        </ul>
    )

}

export default InactiveStocksList;