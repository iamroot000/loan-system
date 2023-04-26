# Generated by Django 4.1.7 on 2023-04-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanager', '0006_alter_loan_table_amount_left_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_table',
            name='amount_left',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='amount_per_day',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='days_left',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='loan_profit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='paid_amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='paid_days',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='progress',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='renew_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='staff_profit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='total_days',
            field=models.IntegerField(default=0, null=True),
        ),
    ]