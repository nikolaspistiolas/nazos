const express = require('express');
const AlgorunSchema = require('../models/algorun_model');
const StockSchema = require("../models/add_remove_stock");
const router = express.Router();

// Routes

// Get
router.get('/', async (req, res) => {
    try {
        const linear_variables = await LinearSchema.find();
        res.json(linear_variables)
    } catch (e) {
        res.status(400).json({message: e.message});
    }
})

module.exports = router;