import React, {useEffect, useState} from 'react';

function AccountInfo(props) {
    const [isLoading, setIsLoading] = useState(true);
    const [loadedInfo, setLoadedInfo] = useState([]);
    useEffect(() => {
        setIsLoading(true);
        fetch(
            '/accountinfo'
        )
            .then((response) => {
                return response.json();
            })
            .then((data) => {

                console.log(data[0])
                setIsLoading(false);
                setLoadedInfo(data[0]);
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
        </table>
    )

}

export default AccountInfo;