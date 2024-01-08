import React, {useState,useEffect} from 'react'
import { Link } from 'react-router-dom'
import logo from '../assets/logo.png'
// import Blockchain  from './Blockchain'
// import ConductTransaction from './ConductTransaction'
function App() {
  const [walletInfo,setWalletInfo]=useState({})
  useEffect(
    ()=>{
      fetch('http://localhost:3107/wallet/info').then(response => response.json())
      .then(walletJson=>setWalletInfo(walletJson))
    },[])
  const {address,balance} = walletInfo
  return (
    <div className="App">
      <img className="logo" src={logo} alt="application logo"/>
      <h3>Welcome to our Mechain</h3>
      <br/>
      <Link to="/Blockchain">Blockchain</Link>
      <Link to="/conduct-transaction">Transaction</Link>
      <Link to="/transaction-pool">Transaction History</Link>
      <br/>
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
      {/* <br/>
      <Blockchain/>
      <br/>
      <ConductTransaction /> */}
    </div>
  );
}

export default App;
