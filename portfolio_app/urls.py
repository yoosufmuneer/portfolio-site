from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('', views.project_index, name = 'home'),
    path('<int:pk>/', views.project_detail, name = 'project_detail'),
]