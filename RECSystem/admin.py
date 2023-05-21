from django.contrib import admin
from .models import Researcher
from django.contrib.auth.models import Group



# Remove the uncessary features
admin.site.unregister(Group)
admin.site.site_url = False

# Changes to make it like REC Admin System
admin.site.site_header = "REC System Admin"
admin.site.site_title = "REC System Admin"
admin.site.index_title = "Welcome to the REC System Admin Area"

class UserAdmin(admin.ModelAdmin):
    list_display = ['researcher_id','username','email','password','school','level', 'protocol_code', 
                     'protocol_title', 'principal_investigator', 'minutes_of_proposal', 'revised_copy', 'routing_form', 'adviser_edorsement']
    search_fields = ['researcher_id','username','email','password','school','level', 'protocol_code', 
                     'protocol_title', 'principal_investigator', 'minutes_of_proposal', 'revised_copy', 'routing_form', 'adviser_edorsement']
    
    
    


admin.site.register(Researcher)
