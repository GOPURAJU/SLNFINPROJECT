# Generated by Django 5.0.6 on 2024-07-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slnapp', '0004_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='terms_and_conditions',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='IF_CUSTOMER_PROFILE_BUSINESS',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='existing_loan',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='loan_type',
            field=models.CharField(choices=[('LAP', 'Lap'), ('LABT', 'Labt')], max_length=10),
        ),
    ]
