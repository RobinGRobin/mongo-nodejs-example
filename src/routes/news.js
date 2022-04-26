const express = require('express');
const artSchema = require('../models/news_model');
const router = express.Router();

// create new article
router.post('/article', (req, res) => {
    //res.json(req.body)
    const article = artSchema(req.body);
    article.save()
            .then((data) => {
                res.json(data)
                console.log(data)})
            .catch((error) => {
                res.json({message: error})
                console.log(error)});
});

// list articles
router.get('/article', (req, res) => {
    artSchema.find()
                .then((data) => res.json(data))
                .catch((error) => res.json(error));
});

// get an specific article
router.get('/article_got', (req, res) => {
    const _title = req.body.title;
    artSchema.findOne({title: _title})
                .then((data) => res.json(data))
                .catch((error) => res.json(error));
});

module.exports = router;