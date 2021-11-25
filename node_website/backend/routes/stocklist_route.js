const express = require('express');
const StockSchema = require('../models/singlestock_model');
const router = express.Router();

// Get All
router.get('/', async (req, res) => {
    try {
        const active_stock = await StockSchema.find({active: true});
        const inactive_stock = await StockSchema.find({active: false})
        res.json({active: active_stock,inactive: inactive_stock});
    } catch (e) {
        res.status(500).json({ error:e.message});
    }
})

// Post One
router.post('/', async (req, res) => {
    const stock = new StockSchema({
        symbol: req.body.symbol,
        active: req.body.active
    });
    try {
        const newStock = await stock.save();
        res.status(201).json(newStock);
    } catch (e) {
        res.status(400).json({message: e.message});
        console.log('EERRROOOORRRRRRRR')
    }
})
// Delete One
router.delete('/', async (req, res) =>{
    console.log('It inserts DELETE');
    await StockSchema.deleteOne({symbol:req.body.symbol})
    res.json({deleted:req.body.symbol})
})

// Update One
router.patch('/', async (req, res) =>{
    console.log('It inserts UPDATE');
    console.log(req.body.symbol,req.body.active)
    await StockSchema.updateOne({symbol:req.body.symbol},{active:req.body.active});
    res.json({symbol:req.body.symbol,active:req.body.active})

})

module.exports = router;
