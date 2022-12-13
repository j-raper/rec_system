from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect    # import HTTPResponse Class
from django.contrib import messages                           # alert messages

# Start view function/model
# Request handler

# PAGES
# Login Page
def login(request):
    return render(request, 'login.html')
# Home Page
def home(request):
    return render(request, 'home.html')
# Submit Manuscript Pages
def submit_bscReq(request):
    return render(request, 'submit_bscReq.html')
def submit_recReq(request):
    return render(request, 'submit_recReq.html')
def submit_payment(request):
    return render(request, 'submit_payment.html')
def submit_feedback(request):
    return render(request, 'submit_feedback.html')
def submit_certification(request):
    return render(request, 'submit_certification.html')

# Create-Account Page
def createAcc(request):
    if request.method == 'POST':
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']
        if new_pass == confirm_pass:
            messages.success(request, 'You successfully created an account. You can now login.')
            return render(request, 'createAcc.html')
        else:
            messages.error(request, 'Password and Confirm Password do not match. Please try again.')
    return render(request, 'createAcc.html')
# Forgot-Password Page
def forgotPass(request):
    return render(request, 'forgotPass.html')
# Forgot-Password/Code-Verification Page
def codeVerify(request):
    return render(request, 'codeVerify.html')
# Forgot-Password/Change-Password Page
def changePass(request):
    if request.method == 'POST':
        new_pass = request.POST['new_pass']
        confirm_new_pass = request.POST['confirm_new_pass']
        if new_pass == confirm_new_pass:
            messages.success(request, 'You successfully change your password. You can now login.')
            return render(request, 'changePass.html')
        else:
            messages.error(request, 'Password and Confirm Password do not match. Please try again.')
    return render(request, 'changePass.html')

