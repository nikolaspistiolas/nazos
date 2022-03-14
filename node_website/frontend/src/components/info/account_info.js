import React, {useEffect, useState} from 'react';

function AccountInfo(props) {
    const [isLoading, setIsLoading] = useState(true);
    const [loadedInfo, setLoadedInfo] = useState([]);
    const [linear, setLinear] = useState([])
    const [algo, setAlgo] = useState([])

    useEffect(() => {
        setIsLoading(true);
        fetch(
            '/accountinfo'
        )
            .then((response) => {
                return response.json();
            })
            .then((data) => {

                setLoadedInfo(data[0]);
            });
        fetch(
            '/linear'
        )
            .then((response) => {
                return response.json();
            })
            .then((data) => {

                setLinear(data[0])
            });
        fetch(
            '/tradevariables'
        )
            .then((response) => {
                return response.json();
            })
            .then((data) => {

                console.log(data[0])
                setAlgo(data[0])
                setIsLoading(false);
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
        <table>
            <tr>
                <th>Update Date</th>
                <th className="table-value">{loadedInfo.Date}</th>
            </tr>
            <tr>
                <th>Cash</th>
                <th className="table-value">{loadedInfo.cash}</th>
            </tr>
            <tr>
                <th>Portfolio</th>
                <th className="table-value">{loadedInfo.portfolio_value}</th>
            </tr>
            <tr>
                <th>Big</th>
                <th className="table-value">{linear.big}</th>
            </tr>
            <tr>
                <th>Medium</th>
                <th className="table-value">{linear.medium}</th>
            </tr>
            <tr>
                <th>Small</th>
                <th className="table-value">{linear.small}</th>
            </tr>
            <tr>
                <th>Buy sd</th>
                <th className="table-value">{algo.buy_sd}</th>
            </tr>
            <tr>
                <th>Sell sd</th>
                <th className="table-value">{algo.sell_sd}</th>
            </tr>
            <tr>
                <th>Stop loss</th>
                <th className="table-value">{algo.stop_loss}</th>
            </tr>
        </table>
        
    )

}

export default AccountInfo;