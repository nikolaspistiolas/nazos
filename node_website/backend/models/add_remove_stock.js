const mongoose = require('mongoose');

const StockSchema = mongoose.Schema({
    symbol: {
        type: String,
        required: true
    },
    active: {
        type: Boolean,
        required: true
    },
    subscribeDate: {
        type: Date,
        default: Date.now()
    }
});

module.exports = mongoose.model('StockList', StockSchema);