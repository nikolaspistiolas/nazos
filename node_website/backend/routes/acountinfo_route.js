const express = require('express');
const AccountInfoSchema = require('../models/account_info_model');
const router = express.Router();

router.get('/', async (req, res) => {
    try {
        const accountinfo = await AccountInfoSchema.find(); //.sort({date: -1}).limit(1)
        res.json(accountinfo)
        console.log(accountinfo)
    } catch (e) {
        res.status(400).json({message: e.message});
    }
})

module.exports = router;