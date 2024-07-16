const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Proxy endpoint to Flask application
app.post('/api/predict', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/predict', {
            url: req.body.url
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).send('Error making prediction');
    }
});

const port = 3001;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
