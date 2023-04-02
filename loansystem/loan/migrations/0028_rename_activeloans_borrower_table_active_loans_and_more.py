# Generated by Django 4.1.7 on 2023-03-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0027_remove_loan_table_paiddates_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrower_table',
            old_name='activeLoans',
            new_name='active_loans',
        ),
        migrations.RenameField(
            model_name='borrower_table',
            old_name='borrowerId',
            new_name='borrower_id',
        ),
        migrations.RenameField(
            model_name='borrower_table',
            old_name='completedLoans',
            new_name='completed_loans',
        ),
        migrations.RenameField(
            model_name='loan_payment',
            old_name='loanId',
            new_name='loan_id',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='amountLeft',
            new_name='amount_left',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='amountLoan',
            new_name='amount_loan',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='amountPerDay',
            new_name='amount_per_day',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='daysLeft',
            new_name='days_left',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='dueDate',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='isApproved',
            new_name='is_approved',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='loanId',
            new_name='loan_id',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='loanProfit',
            new_name='loan_profit',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='loanType',
            new_name='loan_type',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='paidAmount',
            new_name='paid_amount',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='paidDays',
            new_name='paid_days',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='renewCount',
            new_name='renew_count',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='startDate',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='tataProfit',
            new_name='tata_profit',
        ),
        migrations.RenameField(
            model_name='loan_table',
            old_name='totalDays',
            new_name='total_days',
        ),
    ]