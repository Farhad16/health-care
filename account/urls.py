from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register_select/', views.register_select, name='register_select'),
    path('register/', views.registerPage, name='register'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('login/', views.loginPage, name='login'),
    path('hospital_dash/', views.hospital_dash, name='hospital_dash'),
    path('hospital_profile/', views.hospital_profile, name='hospital_profile'),
    path('hospital_update/', views.hospital_update, name='hospital_update'),
    path('add_nurse/', views.add_nurse, name='add_nurse'),
    path('update_nurse/<str:pk>/', views.update_nurse, name='update_nurse'),
    path('nurse_list/', views.nurse_list, name='nurse_list'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    path('patient_update/', views.patient_update, name='patient_update'),
    path('hire_nurse/<str:pk>', views.hire_nurse, name='hire_nurse'),
    path('hire_noti/', views.hire_noti, name='hire_noti'),
    path('search_nurse/', views.search_nurse, name='search_nurse'),
    path('nurse_details/<str:pk>/', views.nurse_details, name='nurse_details'),
    path('view_nurse/<str:pk>/', views.view_nurse, name='view_nurse'),
    path('delete_nurse/<str:pk>/', views.delete_nurse, name='delete_nurse'),
    path('nurse_reserve_details/<str:pk>/',
         views.nurse_reserve_details, name='nurse_reserve_details'),
    path('logout/', views.logout_user, name='logout_user'),

]
