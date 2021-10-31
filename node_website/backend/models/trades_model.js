const mongoose = require('mongoose');

const TradesSchema = mongoose.Schema({
    OpenPrice: {
        type: Number,
        required: true
    },
    ClosePrice: {
        type: Number,
        required: false
    },
    Active: {
        type: Boolean,
        required: true,
        default: true
    },
    Amount: {
        type: Number,
        required: true
    },
    Symbol: {
        type: String,
        required: true
    },
    OpenDate: {
        type: Date,
        required: true
    },
    CloseDate: {
        type: Date,
        required: false
    }
});

module.exports = mongoose.model('trades', TradesSchema);