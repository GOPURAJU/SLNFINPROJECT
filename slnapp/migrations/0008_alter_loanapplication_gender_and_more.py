# Generated by Django 5.0.6 on 2024-07-17 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slnapp', '0007_loanapplication_delete_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'single'), ('Married', 'Married'), ('divorced', 'divorced')], max_length=10),
        ),
        migrations.CreateModel(
            name='DocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_card_front', models.ImageField(upload_to='documents/')),
                ('adhar_card_back', models.ImageField(upload_to='documents/')),
                ('pan_card', models.ImageField(upload_to='documents/')),
                ('customer_photo', models.ImageField(upload_to='documents/')),
                ('property_photo1', models.ImageField(upload_to='documents/')),
                ('property_photo2', models.ImageField(upload_to='documents/')),
                ('property_photo3', models.ImageField(upload_to='documents/')),
                ('property_photo4', models.ImageField(upload_to='documents/')),
                ('pay_slips', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('bank_statement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('employee_id_card', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('business_proof1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('business_proof2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('bank_statement_12m', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('business_office_photo', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('itr1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('itr2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('itr3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('address_proof', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('existing_loan_statement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document4', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('personal_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slnapp.loanapplication')),
            ],
        ),
    ]