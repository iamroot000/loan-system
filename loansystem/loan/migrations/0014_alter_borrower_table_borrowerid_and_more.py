# Generated by Django 4.1.7 on 2023-02-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0013_loan_table_status_alter_loan_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower_table',
            name='borrowerId',
            field=models.IntegerField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='loanId',
            field=models.IntegerField(editable=False, unique=True),
        ),
    ]