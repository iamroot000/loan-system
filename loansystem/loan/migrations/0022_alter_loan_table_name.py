# Generated by Django 4.1.7 on 2023-03-14 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0021_loan_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_table',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.borrower_table'),
        ),
    ]
