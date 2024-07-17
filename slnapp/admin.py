from django.contrib import admin
from .models import *
# Register your models here.
class basicdetailadmin(admin.ModelAdmin):
          list_display=['id','FullName','PanNumber','Gender','Email','Date_of_birth','terms_accepted','MaritalStatus','Required_LoanAmount','created_at']
admin.site.register(basicdetailform,basicdetailadmin)



@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'loan_type', 'income_source')
    search_fields = ('first_name', 'last_name', 'pan_card_number', 'aadhar_card_number')


