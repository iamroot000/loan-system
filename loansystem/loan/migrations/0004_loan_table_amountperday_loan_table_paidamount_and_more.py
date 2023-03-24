# Generated by Django 4.1.7 on 2023-02-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_alter_loan_table_amountloan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_table',
            name='amountPerDay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loan_table',
            name='paidAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan_table',
            name='name',
            field=models.CharField(choices=[('test_borrower2', 'test_borrower2'), ('test_borrower3', 'test_borrower3'), ('test_borrower1', 'test_borrower1')], max_length=20),
        ),
    ]
