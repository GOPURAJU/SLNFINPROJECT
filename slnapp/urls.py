from django.contrib import admin
from django.urls import path

from slnapp import views

urlpatterns = [
    
    path('basicdetail/',views.basicdetail,name='basicdetail'),
    path('success/<int:instance_id>/',views.success,name='success'),
    path('lap/',views.loan_application_view,name='lap'),
    path('lap/<int:instance_id>/',views.document_upload,name='lapdoc')
    ]