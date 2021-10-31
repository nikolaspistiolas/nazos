const express = require('express');
const mongoose = require('mongoose');
const app = express();
require('dotenv/config');
const bodyParser = require('body-parser');


// Import routes
const stocksRoute = require('./routes/stocklist_route');
const linearRoute = require('./routes/algotradevariables_route')

//Middleware
app.use(bodyParser.json());
app.use('/stocks', stocksRoute);
app.use('/linear', linearRoute);

// Routes

//Connect to mongodb
mongoose.connect("mongodb://nikolas:gwlGwl1q@134.209.255.171:27017/production?authSource=admin", // process.env.DB_CONNECTION,
    {useNewUrlParser: true},
    ()=>{
    console.log('Connected to db');
});
const db = mongoose.connection
db.on('error', (error)=> console.error(error))
db.once('open', ()=> console.log('Connected to db'))

app.listen(5000);
