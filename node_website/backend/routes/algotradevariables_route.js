const express = require('express');
const AlgorunSchema = require('../models/algotradevariables_model');
const router = express.Router();

// Routes

// Get
router.get('/', async (req, res) => {
    try {
        const linear_variables = await AlgorunSchema.find();
        res.json(linear_variables)
    } catch (e) {
        res.status(400).json({message: e.message});
    }
})

module.exports = router;