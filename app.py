# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # SQLite database file
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

# db = SQLAlchemy(app)

# # Define a model (example)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

# # Create the database and tables (run this once to set up the database)
# with app.app_context():
#     db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

























from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Blog(db.Model):
    class Blog(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        image = db.Column(db.String(20), nullable=True)
        category = db.Column(db.String(100), nullable=False)
        summary = db.Column(db.String(255), nullable=False)
        content = db.Column(db.Text, nullable=False)
        draft = db.Column(db.Boolean, default=False)
        author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Blog('{self.title}', '{self.category}', '{self.author}')"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/dashboard_doctor')
def dashboard_doctor():
    blogs = Blog.query.filter_by(author='doctor').all()
    return render_template('doctor_dashboard.html', blogs=blogs)

@app.route('/patient_dashboard')
def patient_dashboard():
    blogs = Blog.query.filter_by(draft=False).all()
    return render_template('doctor_dashboard.html', blogs=blogs)

@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        image = request.form['image'] if 'image' in request.form else None
        category = request.form['category']
        summary = request.form['summary']
        content = request.form['content']
        draft = 'draft' in request.form
        author = 'doctor'  # In a real application, this should be dynamically set
        new_blog = Blog(title=title, image=image, category=category, summary=summary, content=content, draft=draft, author=author)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('doctor_dashboard'))
    return render_template('create_blog.html')

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('blog_detail.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)