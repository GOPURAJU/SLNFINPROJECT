from django.db import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import random
import string




def validate_pan(value):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid PAN number format')
class basicdetailform(models.Model):
          Gender_choices=[('Male','Male'),('Female','Female')]
          Marital_Status=[('Single','Single'),('Married','Married'),('Divorced','Divorced')]
          FullName=models.CharField(max_length=25)
          PanNumber=models.CharField(max_length=10,validators=[validate_pan])
          Gender=models.CharField(max_length=10,choices=Gender_choices,default='Male')
          Email=models.EmailField()
          Date_of_birth=models.DateField()
          MaritalStatus=models.CharField(max_length=10,choices=Marital_Status,default='Single')
          Required_LoanAmount=models.DecimalField(max_digits=50,decimal_places=2)
          terms_accepted=models.BooleanField(default=False)
          created_at = models.DateTimeField(auto_now_add=True)
          random_number = models.CharField(max_length=6, blank=True)
         
          def __str__(self):
                  return f"{self.FullName}"
          
          def save(self, *args, **kwargs):
            if not self.random_number:
               self.random_number = ''.join(random.choices(string.digits, k=6))
            super().save(*args, **kwargs)









# from django.db import models

class LoanApplication(models.Model):
    LOAN_TYPE_CHOICES = [
        ('LAP', 'Loan Against Property'),
        ('LAPBT', 'Loan Against Property with Business Tenure'),
    ]
    INCOME_SOURCE_CHOICES = [
        ('JOB', 'Job'),
        ('BUSINESS', 'Business'),
    ]
    
    # Basic Information
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    pan_card_number = models.CharField(max_length=10)
    aadhar_card_number = models.CharField(max_length=12)
    marital_status = models.CharField(max_length=10,choices=[('Single','single'),('Married','Married'),('divorced','divorced')])
    email_id = models.EmailField()
    current_address = models.TextField()
    current_address_pincode = models.CharField(max_length=6)
    aadhar_address = models.TextField()
    aadhar_pincode = models.CharField(max_length=6)

    # Job-related Fields
    income_source = models.CharField(max_length=10, choices=INCOME_SOURCE_CHOICES)
    net_salary_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_type = models.CharField(max_length=50, null=True, blank=True)
    job_joining_date = models.DateField(null=True, blank=True)
    job_location = models.CharField(max_length=100, null=True, blank=True)
    total_job_experience = models.IntegerField(null=True, blank=True)

    # Business-related Fields
    net_income_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    business_type = models.CharField(max_length=50, null=True, blank=True)
    business_establishment_date = models.DateField(null=True, blank=True)
    gst_certificate = models.BooleanField(default=False)
    gst_number = models.CharField(max_length=15, null=True, blank=True)
    nature_of_business = models.TextField(null=True, blank=True)
    turnover_in_lakhs_per_year = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Additional Fields
    property_value = models.DecimalField(max_digits=15, decimal_places=2)
    required_loan_amount = models.DecimalField(max_digits=15, decimal_places=2)
    existing_loan = models.BooleanField(default=False)
    existing_loan_details = models.CharField(max_length=100, null=True, blank=True)
    ref1_name = models.CharField(max_length=100)
    ref1_mobile = models.CharField(max_length=15)
    ref2_name = models.CharField(max_length=100)
    ref2_mobile = models.CharField(max_length=15)
    remarks = models.TextField(null=True, blank=True)

    # Co-Applicant Fields
    co_applicant_first_name = models.CharField(max_length=50, null=True, blank=True)
    co_applicant_last_name = models.CharField(max_length=50, null=True, blank=True)
    co_applicant_gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    co_applicant_age = models.IntegerField(null=True, blank=True)
    co_applicant_relationship = models.CharField(max_length=50, null=True, blank=True)
    co_applicant_mobile_number = models.CharField(max_length=15, null=True, blank=True)
    co_applicant_email_id = models.EmailField(null=True, blank=True)
    co_applicant_occupation = models.CharField(max_length=50, null=True, blank=True)
    co_applicant_net_income_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class DocumentUpload(models.Model):
    personal_details = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    adhar_card_front = models.ImageField(upload_to='documents/')
    adhar_card_back = models.ImageField(upload_to='documents/')
    pan_card = models.ImageField(upload_to='documents/')
    customer_photo = models.ImageField(upload_to='documents/')
    property_photo1 = models.ImageField(upload_to='documents/')
    property_photo2 = models.ImageField(upload_to='documents/')
    property_photo3 = models.ImageField(upload_to='documents/')
    property_photo4 = models.ImageField(upload_to='documents/')
    pay_slips = models.FileField(upload_to='documents/', null=True, blank=True)
    bank_statement = models.FileField(upload_to='documents/', null=True, blank=True)
    employee_id_card = models.ImageField(upload_to='documents/', null=True, blank=True)
    business_proof1 = models.FileField(upload_to='documents/', null=True, blank=True)
    business_proof2 = models.FileField(upload_to='documents/', null=True, blank=True)
    bank_statement_12m = models.FileField(upload_to='documents/', null=True, blank=True)
    business_office_photo = models.ImageField(upload_to='documents/', null=True, blank=True)
    itr1 = models.FileField(upload_to='documents/', null=True, blank=True)
    itr2 = models.FileField(upload_to='documents/', null=True, blank=True)
    itr3 = models.FileField(upload_to='documents/', null=True, blank=True)
    address_proof = models.FileField(upload_to='documents/', null=True, blank=True)
    existing_loan_statement = models.FileField(upload_to='documents/', null=True, blank=True)
    other_document1 = models.FileField(upload_to='documents/', null=True, blank=True)
    other_document2 = models.FileField(upload_to='documents/', null=True, blank=True)
    other_document3 = models.FileField(upload_to='documents/', null=True, blank=True)
    other_document4 = models.FileField(upload_to='documents/', null=True,blank=True)

    #coapplicant documents
    
