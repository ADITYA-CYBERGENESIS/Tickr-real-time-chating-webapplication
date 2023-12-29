from django.urls import path
from . import views

urlpatterns=[
    path('registration',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('emailactivation',views.emailactivation,name='emailactivation'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    path('activation/<str:username>/<str:uniqueid>',views.activation,name='activation'),
    path('reset/<str:username>/<str:uniqueid>',views.resetpassword)
    
  ]