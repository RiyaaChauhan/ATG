
from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms.signup_form import SignUpForm
from users.forms.blog_post_form import BlogPostForm
from users.models import BlogPost, BlogCategory

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_doctor:
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def doctor_dashboard(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_dashboard.html', {'posts': posts})

def patient_dashboard(request):
    categories = BlogCategory.objects.all()
    return render(request, 'patient_dashboard.html', {'categories': categories})
def doctor_login(request):
    return render(request, 'doctor_login.html')

def patient_login(request):
    return render(request, 'patient_login.html')

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('doctor_dashboard')
    else:
         form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

def view_category(request, category_id):
    category = BlogCategory.objects.get(id=category_id)
    posts = BlogPost.objects.filter(category=category, is_draft=False)
    return render(request, 'view_category.html', {'category': category, 'posts': posts})
