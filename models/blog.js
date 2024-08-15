// Example schema for blogs
const Blog = {
    id: Number,
    title: String,
    image_url: String,
    category: String,
    summary: String,
    content: String,
    isDraft: Boolean,
    createdBy: Number, // User ID of the doctor who created it
};

module.exports = Blog;
