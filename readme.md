# Multi-Login System

This project is a multi-login system that supports two types of users: **Doctors** and **Patients**. It allows users to log in based on their role, providing a personalized experience and access to relevant features.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Role-based Authentication:** Supports two types of users: Doctors and Patients.
- **Custom Dashboards:** After login, users are redirected to role-specific dashboards.
- **Blog System (Doctor-specific):** 
  - Doctors can create blog posts with fields: Title, Image, Category, Summary, and Content.
  - Doctors can mark posts as drafts and view their own published and draft posts.
- **Patient View:**
  - Patients can view all published blog posts categorized by category.
  - Each post shows the Title, Image, and a Summary truncated to 15 words.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django, Flask
- **Database:** SQL for storing user credentials and blog data
- **Authentication:** Role-based login system

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/RiyaaChauhan/multi_login.git
    cd multi_login
    ```

2. Install dependencies:

    ```bash
    npm install  # For Node.js
    pip install -r requirements.txt  # For Python/Django/Flask
    ```

3. Set up the database:
    - Ensure you have SQL installed and running.
    - Run the SQL scripts to create necessary tables.

4. Start the development server:

    ```bash
    npm start  # For Node.js
    python manage.py runserver  # For Django/Flask
    ```

5. Open your browser and navigate to `http://localhost:8000` (or your designated port).

## Usage

1. **Doctor Login:**
   - Doctors can log in, create blog posts, and manage their published or draft posts.

2. **Patient Login:**
   - Patients can log in and view all published blog posts, categorized for easy navigation.

3. **Creating a Blog Post:**
   - Doctors can add a new post with the following fields:
     - Title
     - Image
     - Category
     - Summary
     - Content
   - Posts can be saved as drafts for later editing or published immediately.

4. **Viewing Blog Posts:**
   - Patients can browse published blog posts. Each post includes the title, image, and a truncated summary for a quick overview.

## Project Structure

```plaintext
.
├── templates/                # Contains HTML files
├── static/                   # Contains static files like CSS, JS, Images
├── models/                   # Database models for users and blogs
├── routes/                   # Backend routes for handling login, blog CRUD operations
├── app.js                    # Main application logic (if using Node.js)
├── README.md                 # Project documentation
└── database.sql              # SQL file for setting up the database