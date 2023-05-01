from django.contrib import admin
from .models import Researcher

admin.site.site_header = "REC System Admin"
admin.site.site_title = "REC System Admin"
admin.site.index_title = "Welcome to the REC System Admin Area"

class UserAdmin(admin.ModelAdmin):
    list_display = ['researcher_id','username','email','password','school','level', 'protocol_code', 
                     'protocol_title', 'principal_investigator', 'minutes_of_proposal', 'revised_copy', 'routing_form', 'adviser_edorsement']
    search_fields = ['researcher_id','username','email','password','school','level', 'protocol_code', 
                     'protocol_title', 'principal_investigator', 'minutes_of_proposal', 'revised_copy', 'routing_form', 'adviser_edorsement']

admin.site.register(Researcher)
