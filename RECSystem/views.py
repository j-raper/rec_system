from django.shortcuts import render, redirect
from django.contrib import messages                           # alert messages
from django.contrib.auth.models import User
from .models import Researcher
from django.urls import path 
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Start view function/model
# Request handler
def handle_uploaded_file(f):  
    with open('RECSystem/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

# Login Page
def user_login(request):
    if request.method == 'POST':
        # input from user
        username_login = request.POST['username']               
        password_login = request.POST['password']

        # data from database
        rec_admin = authenticate(request, username=username_login, password=password_login)
        researcher = Researcher.objects.filter(username=username_login, password=password_login).exists()

        if rec_admin is not None:
            login(request, rec_admin)
            messages.success(request, 'REC ADMIN')
            return redirect('admin/')
        elif researcher:
            return render(request, 'researcher\home.html')              
        else:
            messages.error(request, 'Invalid Username or Password.')
    return render(request, 'login.html') 
    
# Home Page
def home(request):
    return render(request, 'researcher\home.html')

# About Us
def aboutUs(request):
    return render(request, 'researcher\\aboutUs.html')

# Contact Us
def contactUs(request):
    return render(request, 'researcher\contactUs.html')

# User Settings
def icon(request):
    return render(request, 'researcher\icon.html') 

# Success
def successful(request):
        return render(request, 'researcher\successful.html') 
# Pass    
def changePass(request):
    if request.method == 'POST':
        password = request.POST['password']
        new_pass = request.POST['new_pass']
        confnew_pass = request.POST['confnew_pass']
        
        if Researcher.objects.filter(password=password).exists():
            if new_pass == confnew_pass:
                # Get the first Researcher object with the given password
                researcher = Researcher.objects.filter(password=password).first()
                # Update the password field
                researcher.password = new_pass
                # Save the changes to the database
                researcher.save()
                
                messages.success(request, 'You successfully change your password. You can now login again.')
                return render(request, 'researcher/changePass.html')
            else:
                messages.error(request, 'Password and Confirm Password do not match. Please try again.')  
        else:
            messages.error(request, 'Old Password is incorrect. Please try again.')               
    # Return the newPass.html template for GET requests
    return render(request, 'researcher/changePass.html')

# Submit Manuscript Pages
def submit_bscReq(request):
    if request.method == "POST":
        protocol_title=request.POST.get('protocol_title')
        principal_investigator=request.POST.get('principal_investigator')
        minutes_of_proposal=request.FILES["minutes_of_proposal"]
        revised_copy=request.FILES["revised_copy"]
        routing_form=request.FILES["routing_form"]
        adviser_edorsement=request.FILES["adviser_edorsement"]

        handle_uploaded_file(revised_copy)
        handle_uploaded_file(routing_form)
        handle_uploaded_file(adviser_edorsement)
    
        Researcher.objects.update(protocol_title=protocol_title, 
                                  principal_investigator=principal_investigator, 
                                  minutes_of_proposal=minutes_of_proposal,
                                  revised_copy=revised_copy, 
                                  routing_form=routing_form, 
                                  adviser_edorsement=adviser_edorsement)
        
        messages.success(request, 'You successfully submitted your Basic Requirements. You can now proceed to REC Requirements.')
    return render(request, 'researcher\submit_bscReq.html')

def submit_recReq(request):
    if request.method == "POST":
        curriculum_vitae=request.FILES["curriculum_vitae"]
        research_agenda=request.FILES["research_agenda"]
        grades=request.FILES["grades"]
        REC_FO_OO23=request.FILES["REC_FO_OO23"]
        REC_FO_OO24=request.FILES["REC_FO_OO24"]
        REC_FO_OO25=request.FILES["REC_FO_OO25"]
        REC_FO_OO26=request.FILES["REC_FO_OO26"]
        REC_FO_OO27=request.FILES["REC_FO_OO27"]
        REC_FO_OO57=request.FILES["REC_FO_OO57"]
        REC_FO_OO57B=request.FILES["REC_FO_OO57B"]
        REC_FO_OO58=request.FILES["REC_FO_OO58"]

        handle_uploaded_file(curriculum_vitae)
        handle_uploaded_file(research_agenda)
        handle_uploaded_file(grades)
        handle_uploaded_file(REC_FO_OO23)
        handle_uploaded_file(REC_FO_OO24)
        handle_uploaded_file(REC_FO_OO25)
        handle_uploaded_file(REC_FO_OO26)
        handle_uploaded_file(REC_FO_OO27)
        handle_uploaded_file(REC_FO_OO57)
        handle_uploaded_file(REC_FO_OO57B)
        handle_uploaded_file(REC_FO_OO58)
    
        Researcher.objects.update(curriculum_vitae=curriculum_vitae, 
                                  research_agenda=research_agenda, 
                                  grades=grades,
                                  REC_FO_OO23=REC_FO_OO23, 
                                  REC_FO_OO24=REC_FO_OO24, 
                                  REC_FO_OO25=REC_FO_OO25, 
                                  REC_FO_OO26=REC_FO_OO26, 
                                  REC_FO_OO27=REC_FO_OO27, 
                                  REC_FO_OO57=REC_FO_OO57, 
                                  REC_FO_OO57B=REC_FO_OO57B, 
                                  REC_FO_OO58=REC_FO_OO58)
        
        messages.success(request, 'You successfully submitted your REC Requirements. You can now proceed to Payment.')
    return render(request, 'researcher\submit_recReq.html')

def submit_payment(request):
    if request.method == "POST":
        payment = request.FILES["payment"]

        handle_uploaded_file(payment)

        Researcher.objects.update(payment=payment)

        messages.success(request, 'You successfully submitted your Proof of Payment.')
    return render(request, 'researcher\submit_payment.html')

def submit_feedback(request):
    if request.method == "POST":
        revised_manuscript = request.FILES["revised_manuscript"]

        handle_uploaded_file(revised_manuscript)

        Researcher.objects.update(revised_manuscript=revised_manuscript)
        messages.success(request, 'You successfully submitted your Revised Manuscript.')
    return render(request, 'researcher\submit_feedback.html')

def download_certification(request):
    return render(request, 'researcher\download_certification.html')

# Create-Account Page
def createAcc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST['username']
        email = request.POST['email']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']

        #check username exists
        researcher_username = Researcher.objects.filter(username=username).exists()

        if name == 'signup_researcher':
            if researcher_username:
                messages.error(request, 'Username already exists.')
            elif new_pass == confirm_pass:
                researcher = Researcher()
                researcher.username=request.POST.get('username')
                researcher.email=request.POST.get('email')
                researcher.password=request.POST.get('confirm_pass')
                researcher.school=request.POST.get('school')
                researcher.level=request.POST.get('level')
                researcher.save()

                messages.success(request, 'You successfully created an account. You can now login.')
                return render(request, 'createAcc.html')
            else:
                messages.error(request, 'Password and Confirm Password do not match. Please try again.')
        
        elif name == 'signup_rec':
            try:
                if new_pass == confirm_pass:
                    new_admin = User.objects.create_superuser(username, email, confirm_pass)
                    new_admin.first_name=request.POST.get('firstname')
                    new_admin.last_name=request.POST.get('lastname')
                    new_admin.save()

                    messages.success(request, 'You successfully created an account. You can now login.')
                    return render(request, 'createAcc.html')
                else:
                    messages.error(request, 'Password and Confirm Password do not match. Please try again.')
            except IntegrityError as error:
                messages.error(request, 'Username already exists.')
                return render(request, 'createAcc.html')
    return render(request, 'createAcc.html')

# Forgot-Password Page
def forgotPass(request):
    return render(request, 'forgotPass.html')
# Forgot-Password/Code-Verification Page
def codeVerify(request):
    return render(request, 'codeVerify.html')
# Forgot-Password/Change-Password Page
def newPass(request):
    if request.method == 'POST':
        new_pass = request.POST['new_pass']
        confirm_new_pass = request.POST['confirm_new_pass']
        if new_pass == confirm_new_pass:
            messages.success(request, 'You successfully change your password. You can now login.')
            return render(request, 'newPass.html')
        else:
            messages.error(request, 'Password and Confirm Password do not match. Please try again.')
    return render(request, 'newPass.html')
