import React, {useState} from 'react';
import { Input } from 'react-nice-inputs'
import axios from "axios";




function InputStock(props){

    const [state, setState] = useState('OK')
    console.log(state)
    return(
        <form>
            <label>
                Add Stock:
                <input type="text" name="Add Stocks" />
            </label>
            <input type="submit" value="Submit" />
        </form>

    )

}

export default InputStock;