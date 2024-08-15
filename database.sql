-- User table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('doctor', 'patient') NOT NULL
);

-- Blog table
CREATE TABLE blogs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    image_url VARCHAR(255),
    category VARCHAR(100),
    summary TEXT,
    content TEXT,
    is_draft BOOLEAN,
    created_by INT,
    FOREIGN KEY (created_by) REFERENCES users(id)
);
