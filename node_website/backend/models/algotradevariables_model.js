const mongoose = require('mongoose');

const LinearSchema = mongoose.Schema({
    big: {
        type: Number,
        required: true
    },
    medium: {
        type: Number,
        required: true
    },
    small: {
        type: Number,
        required: true
    },
    big_sd: {
        type: Number,
        required: true
    },
    medium_sd: {
        type: Number,
        required: true
    },
    small_sd: {
        type: Number,
        required: true
    },
    stoploss: {
        type: Number,
        required: true
    },
    subscribeDate: {
        type: Date,
        default: Date.now()
    }
});

module.exports = mongoose.model('algotradevariables', LinearSchema);