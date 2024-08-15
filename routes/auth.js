const express = require('express');
const router = express.Router();

// Example User Model (You can replace this with your actual user model)
const User = require('../models/User');

// Signup Route
router.post('/signup', async (req, res) => {
    try {
        const { username, password, role } = req.body; // role can be 'doctor' or 'patient'
        // Add user creation logic here
        const newUser = new User({ username, password, role });
        await newUser.save();
        res.redirect('/login'); // Redirect to login page after signup
    } catch (error) {
        console.error(error);
        res.status(500).send('Server error');
    }
});

// Login Route
router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        // Add login logic here (e.g., find user, check password, set session)
        const user = await User.findOne({ username });
        if (user && user.password === password) {
            req.session.user = user; // Set user session
            res.redirect('/dashboard'); // Redirect to dashboard after login
        } else {
            res.status(401).send('Invalid credentials');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Server error');
    }
});

// Logout Route
router.get('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            return res.status(500).send('Failed to log out');
        }
        res.redirect('/login');
    });
});

module.exports = router;
