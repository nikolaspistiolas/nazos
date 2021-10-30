const mongoose = require('mongoose');

const LinearSchema = mongoose.Schema({
    big: {
        type: Integer,
        required: true
    },
    medium: {
        type: Integer,
        required: true
    },
    small: {
        type: Integer,
        required: true
    },
    big_sd: {
        type: Double,
        required: true
    },
    medium_sd: {
        type: Double,
        required: true
    },
    small_sd: {
        type: Double,
        required: true
    },
    stoploss: {
        type: Double,
        required: true
    },
    subscribeDate: {
        type: Date,
        default: Date.now()
    }
});

module.exports = mongoose.model('LinearVriables', LinearSchema);