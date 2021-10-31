const mongoose = require('mongoose');

const StockDataSchema = mongoose.Schema({
    Open: {
        type: Number,
        required: true
    },
    High: {
        type: Number,
        required: true
    },
    Low: {
        type: Number,
        required: true
    },
    Close: {
        type: Number,
        required: true
    },
    Volume: {
        type: Number,
        required: true
    },
    Symbol: {
        type: String,
        required: true
    },
    Date: {
        type: Date,
        required: true
    }
});

module.exports = mongoose.model('stockdata', StockDataSchema);