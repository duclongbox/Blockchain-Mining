import React, {useState,useEffect} from 'react'
import { Button } from 'react-bootstrap'
import Block from './Block'

const PAGE_RANGE = 3

function Blockchain() {
    const [blockchain,setBlockchain] =useState([])
    const [blockchainLength, setBlockchainLength]=useState(0)

    const fetchBlockchainPage = (start,end) => {
        fetch(`http://localhost:3107/blockchain/range?start=${start}&end=${end}`).then(response => response.json())
        .then(jsonData => setBlockchain(jsonData));
    }

    useEffect(
        ()=>{
           fetchBlockchainPage(0 ,PAGE_RANGE)
            fetch('http://localhost:3107/blockchain/length').then(response => response.json())
            .then(jsonData => setBlockchainLength(jsonData));
    },[])
    const buttonNumbers =[]
    for(let i=0; i<(blockchainLength/PAGE_RANGE);i++){
        buttonNumbers.push(i)
    }
    return(
        <div className="Blockchain">
            <h3>Blockchain</h3>
            <div>
                {blockchain.map((block)=>{
                    return <Block key={block.hash} block={block}/>
                })}
            </div>
            <div>
                {
                    buttonNumbers.map(number =>{
                        const start = number*PAGE_RANGE
                        const end = (number+1)* PAGE_RANGE
                        return(
                            <span key={number} onClick={()=>fetchBlockchainPage(start,end)}>
                                <Button size="sm" variant="danger" >
                                    {number+1}
                                </Button>{' '}
                            </span>
                        )
                    })
                }
            </div>
        </div>
    )
}
export default Blockchain