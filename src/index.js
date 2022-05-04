const express = require('express');
const app = express();  // Retorno del objeto de la aplicación
const mongoose = require('mongoose');
require('dotenv').config();
const path = require('path');
const articleRoutes = require("./routes/news")
const port = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname,'views'));

// middleware
app.use(express.json());

// Routes
app.use("/", articleRoutes);

// Mongo DB Connection
mongoose.connect(process.env.MONGODB_URI)
        .then(() => console.log('Connected to Mongo DB Atlas'))
        .catch((error) => console.error(error));

app.listen(port, () => {
    console.log('Server on port ', port)
})