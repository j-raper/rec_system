from django.db import models
from django.db import connections
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Database - phpMyAdmin
# connecting user details from database

# User
class Researcher(models.Model):
    researcher_id=models.AutoField(primary_key=True, verbose_name='Protocol Code')
    username=models.CharField(unique=True, max_length=100, verbose_name='Username')
    email=models.CharField(max_length=100, verbose_name='Researcher Email')
    password=models.CharField(max_length=100, verbose_name='Researcher Password')
    school=models.CharField(max_length=100, verbose_name='Researcher School')
    level=models.CharField(max_length=100, verbose_name='Researcher Level')

    #basic requirements
    protocol_title = models.CharField(max_length=100, verbose_name='Research Title')
    principal_investigator = models.TextField(max_length=1000, verbose_name='Principal Investigator/s')
    minutes_of_proposal = models.FileField(upload_to="media/", verbose_name="Minutes of Proposal Defense")
    revised_copy = models.FileField(upload_to="media/", verbose_name="Revised Copy")
    routing_form = models.FileField(upload_to="media/", verbose_name="Routing Form")
    adviser_edorsement = models.FileField(upload_to="media/", verbose_name="Adviser's Endorsement for Ethics Review")

    #rec requirements
    curriculum_vitae = models.FileField(upload_to="media/", verbose_name="Updated Curriculum Vitae (CV) of the Adviser(s) and Researcher(s)")
    research_agenda = models.FileField(upload_to="media/", verbose_name="Updated Research Agenda of the Program")
    grades = models.FileField(upload_to="media/", verbose_name="Grades")
    REC_FO_OO23 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO23")
    REC_FO_OO24 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO24")
    REC_FO_OO25 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO25")
    REC_FO_OO26 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO26")
    REC_FO_OO27 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO27")
    REC_FO_OO57 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO57")
    REC_FO_OO57B = models.FileField(upload_to="media/", verbose_name="REC_FO_OO57B")
    REC_FO_OO58 = models.FileField(upload_to="media/", verbose_name="REC_FO_OO58")

    #payment
    payment = models.FileField(upload_to="media/", verbose_name="Payment")

    #payment
    revised_manuscript = models.FileField(upload_to="media/", verbose_name="Revised Manuscript")

    def __str__(self):
        return self.school + ' | ' + self.username
    
class Meta:
    db_table="researchers"
