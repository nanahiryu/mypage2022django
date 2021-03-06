from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
]
