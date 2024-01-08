import React from 'react';
import ReactDOM from 'react-dom/client';
import { Router, Switch, Route } from 'react-router-dom'
import './index.css';
import history from './history';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTtransaction from './components/ConductTransaction'
import TransactionPool from './components/TransactionPool';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  //<React.StrictMode>
    <Router history={history}>
      <Switch>
        <Route path='/' exact component={App} />
        <Route path='/blockchain' component={Blockchain}/>
        <Route path='/conduct-transaction' component={ConductTtransaction}/>
        <Route path='/transaction-pool' component={TransactionPool}/>
      </Switch>
    </Router>
  //</React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
 