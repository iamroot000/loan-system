# Generated by Django 4.1.7 on 2023-04-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanager', '0005_alter_loan_payment_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_table',
            name='amount_left',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='amount_loan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='amount_per_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='loan_type',
            field=models.CharField(choices=[('custom', 'Custom'), ('daily', 'Daily')], max_length=8),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='total_days',
            field=models.IntegerField(default=0),
        ),
    ]
