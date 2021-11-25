import React from 'react';
import { Input } from 'react-nice-inputs'
import axios from "axios";




function InputStock(props){

    return(
        <Input type="text" // type is required
               name="some-input" // is required
               classList={ [ 'col', 'sm-12', 'md-4' ] } // is required
               onChange={ (value) => { this.setState({ yourParentComponentState: value }) } } // is required
               attrs={ { placeholder: 'enter a value' } }
               isValid="true"
        />
    )

}

export default InputStock;