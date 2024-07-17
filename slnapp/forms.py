from django import forms
from .models import *
from django.utils import timezone
from datetime import timedelta

class BasicDetailForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = basicdetailform
        fields = '__all__'
        widgets = {
            'FullName': forms.TextInput(attrs={'class': 'form-control'}),
            'PanNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'MaritalStatus': forms.Select(attrs={'class': 'form-control'}),
            'Required_LoanAmount': forms.NumberInput(attrs={'class': 'form-control'}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'random_number': forms.HiddenInput(),

        }
        error_messages = {
            'FullName': {'required': 'Full name is required.'},
            'PanNumber': {'required': 'Pan number is required.'},
            'Gender': {'required': 'Gender is required.'},
            'Email': {'required': 'Email is required.'},
            'Date_of_birth': {'required': 'Date of birth is required.'},
            'MaritalStatus': {'required': 'Marital status is required.'},
            'Required_LoanAmount': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }

    def clean(self):
        cleaned_data = super().clean()
        pan_number = cleaned_data.get('PanNumber')

        # Check for previous applications within the last three months
        three_months_ago = timezone.now() - timedelta(days=90)
        recent_applications = basicdetailform.objects.filter(
            PanNumber=pan_number,
            created_at__gte=three_months_ago
        )

        if recent_applications.exists():
            raise forms.ValidationError("You have already applied within the last three months. Please reapply after three months.")

        return cleaned_data
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
          instance.save()
        return instance





from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = '__all__'
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control'}),
            'current_address_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_address': forms.Textarea(attrs={'class': 'form-control'}),
            'aadhar_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'income_source': forms.Select(attrs={'class': 'form-control'}),
            'net_salary_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_type': forms.TextInput(attrs={'class': 'form-control'}),
            'job_joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'total_job_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            # Business fields
            'net_income_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_type': forms.TextInput(attrs={'class': 'form-control'}),
            'business_establishment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gst_certificate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
            'nature_of_business': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'turnover_in_lakhs_per_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'existing_loan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'existing_loan_details': forms.TextInput(attrs={'class': 'form-control'}),
            'ref1_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref1_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
            # Co-Applicant fields
            'co_applicant_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_gender': forms.Select(attrs={'class': 'form-control'}),
            'co_applicant_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'co_applicant_relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'co_applicant_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_net_income_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
        }




class LapDocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = '__all__'
        widgets = {
            'adhar_card_front': forms.FileInput(attrs={'class': 'form-control'}),
            'adhar_card_back': forms.FileInput(attrs={'class': 'form-control'}),
            'pan_card': forms.FileInput(attrs={'class': 'form-control'}),
            'customer_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'property_photo1': forms.FileInput(attrs={'class': 'form-control'}),
            'property_photo2': forms.FileInput(attrs={'class': 'form-control'}),
            'property_photo3': forms.FileInput(attrs={'class': 'form-control'}),
            'property_photo4': forms.FileInput(attrs={'class': 'form-control'}),
            'pay_slips': forms.FileInput(attrs={'class': 'form-control'}),
            'bank_statement': forms.FileInput(attrs={'class': 'form-control'}),
            'employee_id_card': forms.FileInput(attrs={'class': 'form-control'}),
            'business_proof1': forms.FileInput(attrs={'class': 'form-control'}),
            'business_proof2': forms.FileInput(attrs={'class': 'form-control'}),
            'bank_statement_12m': forms.FileInput(attrs={'class': 'form-control'}),
            'business_office_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'itr1': forms.FileInput(attrs={'class': 'form-control'}),
            'itr2': forms.FileInput(attrs={'class': 'form-control'}),
            'itr3': forms.FileInput(attrs={'class': 'form-control'}),
            'address_proof': forms.FileInput(attrs={'class': 'form-control'}),
            'existing_loan_statement': forms.FileInput(attrs={'class': 'form-control'}),
            'other_document1': forms.FileInput(attrs={'class': 'form-control'}),
            'other_document2': forms.FileInput(attrs={'class': 'form-control'}),
            'other_document3': forms.FileInput(attrs={'class': 'form-control'}),
            'other_document4': forms.FileInput(attrs={'class': 'form-control'}),
     }