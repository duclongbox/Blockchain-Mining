import React, {useState,useEffect} from 'react'
import logo from '../assets/logo.png'
import Blockchain  from './Blockchain'
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
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
      <br/>
      <Blockchain/>
    </div>
  );
}

export default App;
