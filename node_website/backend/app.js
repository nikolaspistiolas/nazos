const express = require('express');
const mongoose = require('mongoose');
require('dotenv/config');
const bodyParser = require('body-parser');

const app = express();

// Import routes
const accountinfoRoute = require('./routes/acountinfo_route')
const stocksRoute = require('./routes/stocklist_route');
const linearRoute = require('./routes/algotradevariables_route')

//Middleware

app.use(bodyParser.json());
app.use('/stocks', stocksRoute);
app.use('/linear', linearRoute);
app.use('/accountinfo',accountinfoRoute);
// Routes

//Connect to mongodb
mongoose.connect("mongodb://nikolas:gwlGwl1q@134.209.255.171:27017/production?authSource=admin",
    {useNewUrlParser: true},
    ()=>{
    console.log('Connected to db');
});

app.listen(5001);
