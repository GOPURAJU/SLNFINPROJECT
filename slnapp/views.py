

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *

def basicdetail(request):
    if request.method == 'POST':
        form = BasicDetailForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save()
            return redirect('success',instance_id=instance.id)  # Redirect to a success page or another appropriate page
    else:
        form = BasicDetailForm()
    
    return render(request, 'customer/basicdetailform.html', {'form': form})

def success(request, instance_id):
    instance = basicdetailform.objects.get(id=instance_id)
    context = {
        'random_number': instance.random_number if instance.random_number else None,
    }
    return render(request, 'customer/a.html', context)



def loan_application_view(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan_application = form.save()
            return redirect('lapdoc', instance_id=loan_application.id)
    else:
        form = LoanApplicationForm()
    
    return render(request, 'customer/LAPform.html', {'form': form})

def document_upload(request, instance_id):
    personal_details = get_object_or_404(LoanApplication, id=instance_id)
    applicant_document, created = DocumentUpload.objects.get_or_create(personal_details=personal_details)

    if request.method == 'POST':
        form = LapDocumentUploadForm(request.POST, request.FILES, instance=applicant_document)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = LapDocumentUploadForm(instance=applicant_document)
    
    return render(request, 'customer/lapdoc.html', {
        'form': form,
        'incomesource': personal_details.income_source,
        'loan_type': personal_details.loan_type,
    })
