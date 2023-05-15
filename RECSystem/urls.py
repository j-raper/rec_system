from turtle import home
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Start Mapping URL
# URLConfiguration
urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('profile/', views.icon, name='icon'),
    path('successful/', views.successful, name='successful'),
    path('profile/change-password', views.changePass, name='change-password'),
    path('submit-manuscript/basic-requirements', views.submit_bscReq, name='basic-requirements'),
    path('submit-manuscript/rec-requirements', views.submit_recReq, name='rec-requirements'),
    path('submit-manuscript/payment', views.submit_payment, name='payment'),
    path('submit-manuscript/feedback', views.submit_feedback, name='feedback'),
    path('submit-manuscript/certification', views.download_certification, name='certification'),
    path('create-account/', views.createAcc, name='create-account'),
    path('forgot-password/', views.forgotPass, name='forgot-password'),
    path('forgot-password/code-verification/', views.codeVerify, name='code-verification'),
    path('forgot-password/new-password/', views.newPass, name='new-password'),
]

# define url static files
urlpatterns += staticfiles_urlpatterns()
