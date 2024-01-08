import React, {useState} from "react";
import { FormGroup, FormControl, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import history from "../history";
function ConductTransaction(){
    const [amount, setAmount] =useState(0);
    const [recipient, setRecipient] = useState('');
    const updateRecipient = event =>{
        setRecipient(event.target.value)
    }
    const updateAmount = event =>{
        setAmount(Number(event.target.value))
    }
    const submitTransaction =()=>{
        fetch('http://localhost:3107/wallet/transaction',
        {
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({recipient,amount})
        }).then(response=> response.json())
        .then(dataJson=>{
            console.log('submitTransaction',dataJson);
            alert('successful transaction')
            history.push('/transaction-pool')
        })
    }
    return(
        <div className="ConductTransaction">
            <Link to="/">Home</Link>{' '}
            <Link to="/Blockchain">Blockchain</Link>{' '}
            <Link to="/transaction-pool">Transaction History</Link>
            <hr/>
            <h3>Conduct a Transaction</h3>
            <FormGroup>
                <FormControl
                    input="text"
                    placeholder="recipient"
                    value={recipient}
                    onChange={updateRecipient}
                />
            </FormGroup>
            <FormGroup>
                <FormControl
                    input="Number"
                    placeholder="amount"
                    value={amount}
                    onChange={updateAmount}
                />
            </FormGroup>
            <div>
                <Button variant="danger" onClick={submitTransaction}>
                    Submit
                </Button>
            </div>
        </div>
    )
}
export default ConductTransaction;