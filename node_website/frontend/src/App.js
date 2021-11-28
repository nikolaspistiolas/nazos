import React, { Component }  from 'react';
import AllStocks from "./components/stocks/AllStocks";
import AccountInfo from "./components/info/account_info";
import Title from './components/Title';
function App() {

  return (
        <div>
            <Title />
          <div className="parent">

              <div className="row">
                  <AccountInfo />
              </div>
              <div className="row">
              <AllStocks />
              </div>
          </div>
        </div>

  );
}

export default App;
