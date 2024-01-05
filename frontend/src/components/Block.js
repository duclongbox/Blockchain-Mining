import React,{useState} from "react";
import { Button } from 'react-bootstrap';
import { MILLISECOND } from "../config";
import Transaction from "./Transaction";

function ToggleTransactionDisplay({block}){
    const [displayTransaction, setDisplayTransaction] = useState(false)
    const {data} = block
    const toggleDisplay = () =>{
        setDisplayTransaction(!displayTransaction)
    }
    if(displayTransaction){
        return(
            <div>
                {data.map(transaction=>(
                <div key={transaction.id}> 
                    <hr/>
                    <Transaction transaction={transaction}/>
                </div>
                ))}
                <br/>
                <Button variant="danger" size="sm" onClick={toggleDisplay}>
                    Show Less
                </Button>
            </div>
        )
    }
    return(
        <div>
            <br/>
            <Button variant="danger" size="sm" onClick={toggleDisplay}>Show more</Button>
        </div>
    )
}

function Block({block}){
    const {timestamp,hash,data} = block
    const timestampDisplay = new Date(timestamp/MILLISECOND).toLocaleString()
    return (
        <div className="Block">
            <div>Hash : {hash}</div>
            <div>Timestamp: {timestampDisplay}</div>
            <ToggleTransactionDisplay block={block} />
        </div>
    )
}
export default Block;