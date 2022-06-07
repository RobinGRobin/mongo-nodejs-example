const controller = {}
const artSchema = require('../models/news_model');

controller.getInitialPage = (req, res) => {
    artSchema.find()
                .then((data) => {
                    res.render('index',{noticia:data});
                    console.log({noticia:data});
                })
                .catch((error) => res.json(error));
};

module.exports = controller;