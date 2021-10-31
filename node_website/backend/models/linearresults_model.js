const mongoose = require('mongoose');

const LinearSchema = mongoose.Schema({
    symbol: {
        type: String,
        required: true
    },
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
    big_pred: {
        type: Number,
        required: true
    },
    medium_pred: {
        type: Number,
        required: true
    },
    small_pred: {
        type: Number,
        required: true
    },
    Date: {
        type: Date,
        required: true,
        default: Date.now()
    }
});

module.exports = mongoose.model('LinearVriables', LinearSchema);