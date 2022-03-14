const mongoose = require('mongoose');

const LinearSchema = mongoose.Schema({
    buy_sd: {
        type: Number,
        required: true
    },
    sell_sd: {
        type: Number,
        required: true
    },
    stoploss: {
        type: Number,
        required: true
    }
});

module.exports = mongoose.model('algotradevariables', LinearSchema);