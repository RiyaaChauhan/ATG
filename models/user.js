// Example schema for Doctor and Patient users (use SQL or an ORM like Sequelize)
const User = {
    id: Number,
    name: String,
    email: String,
    password: String,
    role: String, // 'doctor' or 'patient'
};

module.exports = User;
