const mongoose = require('mongoose');

const AccountInfoSchema = mongoose.Schema({
    CloseDate: {
        type: Date,
        required: true
    },
    cash: {
        type: String,
        required: true
    },
    portfolio_value: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('account_info', AccountInfoSchema);