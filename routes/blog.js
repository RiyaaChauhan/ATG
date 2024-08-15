const express = require('express');
const router = express.Router();

// Example Blog Model (You can replace this with your actual blog model)
const Blog = require('../models/Blog');

// Create a New Blog Post (only for doctors)
router.post('/new', async (req, res) => {
    try {
        if (req.session.user && req.session.user.role === 'doctor') {
            const { title, content } = req.body;
            const newBlog = new Blog({
                title,
                content,
                author: req.session.user.username,
                createdAt: new Date()
            });
            await newBlog.save();
            res.redirect('/blogs'); // Redirect to blog listing page after creating a post
        } else {
            res.status(403).send('Forbidden: Only doctors can post blogs');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Server error');
    }
});

// View All Blog Posts
router.get('/', async (req, res) => {
    try {
        const blogs = await Blog.find().sort({ createdAt: -1 });
        res.render('blogs', { blogs }); // Pass blogs to the view (blogs.ejs)
    } catch (error) {
        console.error(error);
        res.status(500).send('Server error');
    }
});

// View a Single Blog Post
router.get('/:id', async (req, res) => {
    try {
        const blog = await Blog.findById(req.params.id);
        if (blog) {
            res.render('blog', { blog }); // Pass the blog to the view (blog.ejs)
        } else {
            res.status(404).send('Blog not found');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Server error');
    }
});

module.exports = router;
