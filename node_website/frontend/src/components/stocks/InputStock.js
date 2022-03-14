import React, {useState} from 'react';
import { Input } from 'react-nice-inputs'
import {TextField, Button} from '@material-ui/core';
import styled from "styled-components"

import axios from "axios";

const CssTextField = styled(TextField)({
    '& label.Mui-focused': {
      color: '#2c292b',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'green',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: '#2c292b',
      },
      '&:hover fieldset': {
        borderColor: '#2CBB63',
      },
      '&.Mui-focused fieldset': {
        borderColor: '#2CBB63',
      },
    },
  });


function InputStock(props){

    const [state, setState] = useState('OK')
    console.log(state)
    return(
        <form>
            <label>
                <CssTextField id="outlined-basic" fullWidth inputProps={{ style: { borderColor: '#2CBB63'}}}
                     label="Add stock" variant="outlined" />
            </label>
            <Button variant="outlined">Submit</Button>
        </form>

    )

}

export default InputStock;