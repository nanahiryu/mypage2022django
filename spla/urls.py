from django.urls import path
from . import views

app_name = 'spla'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('weapon_list/', views.WeaponListView.as_view(), name='weapon_list'),
    path('weapon_detail/<int:pk>/',
         views.WeaponDetailView.as_view(), name='weapon_detail'),
    path('main_list', views.MainListView.as_view(), name='main_list'),
    path('main_detail/<int:pk>/', views.MainDetailView.as_view(), name='main_detail'),
    path('sub_list', views.SubListView.as_view(), name='sub_list'),
    path('sub_detail/<int:pk>/', views.SubDetailView.as_view(), name='sub_detail'),
    path('special_list', views.SpecialListView.as_view(), name='special_list'),
    path('special_detail/<int:pk>/',
         views.SpecialDetailView.as_view(), name='special_detail'),
]
