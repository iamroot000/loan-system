# Generated by Django 4.1.7 on 2023-02-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_loan_table_amountleft_loan_table_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_table',
            name='amountLeft',
            field=models.IntegerField(),
        ),
    ]
