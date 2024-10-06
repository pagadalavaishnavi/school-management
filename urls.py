from django.urls import path
from app import views
urlpatterns=[
    path('func1',views.fun),
    path('func2/<str:name>',views.fun2),
    path('add/<int:n1>/<int:n2>',views.add),
    path('add2',views.add2),      
    path('idx',views.sub,name="idx"),
    path('con',views.con,name="ct"),
    path('abo',views.abou,name="ab"),  

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutView, name='logout'),
    
    # Role-specific login URLs
    path('login/student/', views.loginview, {'role': 'student'}, name='student_login'),
    path('login/faculty/', views.loginview, {'role': 'faculty'}, name='faculty_login'),
    path('login/admin/', views.loginview, {'role': 'admin'}, name='admin_login'),
]
