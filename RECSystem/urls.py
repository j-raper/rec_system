from turtle import home
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Start Mapping URL
# URLConfiguration
urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('submit-manuscript/basic-requirements', views.submit_bscReq, name='basic-requirements'),
    path('submit-manuscript/rec-requirements', views.submit_recReq, name='rec-requirements'),
    path('submit-manuscript/payment', views.submit_payment, name='payment'),
    path('submit-manuscript/feedback', views.submit_feedback, name='feedback'),
    path('submit-manuscript/certification', views.submit_certification, name='certification'),
    path('create-account/', views.createAcc, name='create-account'),
    path('forgot-password/', views.forgotPass, name='forgot-password'),
    path('forgot-password/code-verification/', views.codeVerify, name='code-verification'),
    path('forgot-password/change-password/', views.changePass, name='change-password')
    
]

# define url static files
urlpatterns += staticfiles_urlpatterns()