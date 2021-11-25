import React , {useState, useEffect} from "react";
import axios from "axios";
import InactiveStockList from "./InactiveStockList";


function ActiveStocks(props){
    const [isLoading, setIsLoading] = useState(true);
    const [loadedStocks, setLoadedStocks] = useState([]);

    useEffect(() => {
        setIsLoading(true);
        fetch(
            '/stocks'
        )
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log(data);
                const stocks = [];

                for (const key in data['inactive']) {
                    const meetup = {
                        symbol: data['inactive'][key].symbol
                    };

                    stocks.push(meetup);
                }
                console.log(stocks)
                setIsLoading(false);
                setLoadedStocks(stocks);
            });
    }, []);

    if (isLoading) {
        return (
            <section>
                <p>Loading...</p>
            </section>
        );
    }

    return (
        <div>
            <h1>List of InactiveStocks</h1>
            <InactiveStockList stocks={loadedStocks}/>
        </div>
    )
}


export default ActiveStocks;