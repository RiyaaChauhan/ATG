from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

db = SQLAlchemy(app)

# Define a model (example)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Create the database and tables (run this once to set up the database)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

























# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from werkzeug.utils import secure_filename
# import os
# import sqlite3
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///blog.db"
# db=

# # mysql://username:password@server/db
# # app.secret_key = 'your_secret_key'
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # def init_db():
# #     with sqlite3.connect('database.db') as conn:
# #         c = conn.cursor()
# #         c.execute('''
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY,
# #                 first_name TEXT,
# #                 last_name TEXT,
# #                 profile_picture TEXT,
# #                 username TEXT UNIQUE,
# #                 email TEXT UNIQUE,
# #                 password TEXT,
# #                 user_type TEXT,
# #                 address_line1 TEXT,
# #                 city TEXT,
# #                 state TEXT,
# #                 pincode TEXT
# #             )
# #         ''')
# #         c.execute('''
# #             CREATE TABLE IF NOT EXISTS posts (
# #                 id INTEGER PRIMARY KEY,
# #                 title TEXT,
# #                 image TEXT,
# #                 category TEXT,
# #                 summary TEXT,
# #                 content TEXT,
# #                 draft INTEGER,
# #                 author_id INTEGER,
# #                 FOREIGN KEY (author_id) REFERENCES users (id)
# #             )
# #         ''')
# #     conn.close()

# # init_db()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         profile_picture = request.files['profile_picture']
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']
#         user_type = request.form['user_type']
#         address_line1 = request.form['address_line1']
#         city = request.form['city']
#         state = request.form['state']
#         pincode = request.form['pincode']

#         if password != confirm_password:
#             flash('Passwords do not match!')
#             return redirect(url_for('signup'))

#         if profile_picture:
#             filename = secure_filename(profile_picture.filename)
#             profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         else:
#             filename = None

#         with sqlite3.connect('database.db') as conn:
#             c = conn.cursor()
#             c.execute('''
#                 INSERT INTO users (
#                     first_name, last_name, profile_picture, username, email,
#                     password, user_type, address_line1, city, state, pincode
#                 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             ''', (first_name, last_name, filename, username, email, password, user_type, address_line1, city, state, pincode))
#             conn.commit()
#             flash('Signup successful! Please login.')
#             return redirect(url_for('login'))

#     return render_template('signup.html')

# @app.route('/doctor_login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         with sqlite3.connect('database.db') as conn:
#             c = conn.cursor()
#             c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#             user = c.fetchone()
        
#         if user:
#             session['user_id'] = user[0]
#             session['username'] = user[4]
#             session['user_type'] = user[7]
#             if user[7] == 'Patient':
#                 return redirect(url_for('dashboard_patient'))
#             elif user[7] == 'Doctor':
#                 return redirect(url_for('dashboard_doctor'))
#         else:
#             flash('Invalid username or password!')

#     return render_template('login.html')

# @app.route('/dashboard_patient')
# def dashboard_patient():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
    
#     with sqlite3.connect('database.db') as conn:
#         c = conn.cursor()
#         c.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
#         user = c.fetchone()
#         c.execute('SELECT * FROM posts WHERE draft = 0')
#         posts = c.fetchall()

#     return render_template('dashboard_patient.html', user=user, posts=posts)

# @app.route('/dashboard_doctor')
# def dashboard_doctor():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     with sqlite3.connect('database.db') as conn:
#         c = conn.cursor()
#         c.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
#         user = c.fetchone()
#         c.execute('SELECT * FROM posts WHERE author_id = ?', (session['user_id'],))
#         posts = c.fetchall()

#     return render_template('dashboard_doctor.html', user=user, posts=posts)

# @app.route('/create_post', methods=['GET', 'POST'])
# def create_post():
#     if 'user_id' not in session or session['user_type'] != 'Doctor':
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         title = request.form['title']
#         image = request.files['image']
#         category = request.form['category']
#         summary = request.form['summary']
#         content = request.form['content']
#         draft = int(request.form.get('draft', 0))

#         if image:
#             filename = secure_filename(image.filename)
#             image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         else:
#             filename = None

#         with sqlite3.connect('database.db') as conn:
#             c = conn.cursor()
#             c.execute('''
#                 INSERT INTO posts (
#                     title, image, category, summary, content, draft, author_id
#                 ) VALUES (?, ?, ?, ?, ?, ?, ?)
#             ''', (title, filename, category, summary, content, draft, session['user_id']))
#             conn.commit()
#             flash('Post created successfully!')
#             return redirect(url_for('dashboard_doctor'))

#     return render_template('create_post.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
