import React, {useState,useEffect} from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap"
import Transaction from "./Transaction";
import history from "../history";
function TransactionPool(){
    const [transactions, setTransactions] = useState([])

    useEffect(()=>{
        fetch('http://localhost:3107/transactions').then(response=> response.json())
        .then(dataJson=>setTransactions(dataJson))
    },[])
    const fetchMineBlock = () =>{
        fetch('http://localhost:3107/blockchain/mining').then(()=>{
            alert('Success!');
            history.push('/blockchain')
        })
    }
    return(
        <div className="TransactionPool">
            <Link to="/">Home</Link>{' '}
            <Link to="/Blockchain">Blockchain</Link>{' '}
            <Link to="/conduct-transaction">Transaction</Link>
            <hr/>
            <h3>Transaction History</h3>
            <div>
                {
                    transactions.map(
                        transaction =>(
                            <div key={transaction.id}>
                                <hr/>
                                <Transaction transaction={transaction}/>
                            </div>
                        )
                    )
                }
            </div>
            <hr/>
            <Button onClick={fetchMineBlock}>
                Mine A Block of These transaction
            </Button>
        </div>
    )

}

export default TransactionPool