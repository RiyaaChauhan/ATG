from django.urls import path
from .views import signup, doctor_dashboard, patient_dashboard, create_post, view_category

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor-login/', views.doctor_login, name='doctor_login'),
    path('patient-login/', views.patient_login, name='patient_login'),
    path('create_post/', create_post, name='create_post'),
    path('category/<int:category_id>/', view_category, name='view_category'),
]