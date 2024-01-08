import React from "react";

function Transaction({transaction}){
    const {input, output} = transaction;
    const recipients = Object.keys(output)
    console.log(transaction)
    return (
        <div className="Transaction">
            <div>From: {input.address}</div>
            {
                // recipients.map((recipient)=>{
                //     return <div key={recipient}>To: {recipient} | Sent: {output[recipient]} </div>
                // })
                <div key={recipients[1]}>To: {recipients[1]} | Sent: {output[recipients[1]]} </div>
            }
        </div>
    )

}
export default Transaction