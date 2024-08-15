const mysql = require('mysql2');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'your_user_name',
    password: 'your_pass',
    database: 'name_of_your_db'
});

connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database:', err.stack);
        return;
    }
    console.log('Connected to the database');
});



const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const session = require('express-session'); // For session management


app.set('views', path.join(__dirname, 'templates')); // Set 'templates' folder as the views folder

// Middleware for handling form data
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'templates')));

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'login.html'));
});

app.post('/login', (req, res) => {
    const { email, password, role } = req.body;
    if (role === 'doctor') {
        res.redirect('/doctor_dashboard');
    } else {
        res.redirect('/patient_dashboard');
    }
});

app.get('/doctor_dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'doctor_dashboard.html'));
});


app.get('/patient_dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'patient_dashboard.html'));
});

app.get('/create_blog', (req, res) => {
    res.sendFile(__dirname + '/public/create_blog.html');
});


// Logout route to clear the session
app.get('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            return res.send('Error logging out.');
        }
        res.redirect('/');
    });
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});