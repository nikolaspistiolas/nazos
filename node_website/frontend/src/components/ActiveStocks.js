import React , {useState, useEffect} from "react";
import axios from "axios";
import SingleStockActiveList from "./ActiveStockList";
// import SingleStockInactive from "./SingleStockInactive";


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

                for (const key in data['active']) {
                    const meetup = {
                        symbol: data['active'][key].symbol
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
            <h1>List of ActiveStocks</h1>
            <SingleStockActiveList stocks={loadedStocks}/>
        </div>
    )
}


export default ActiveStocks;