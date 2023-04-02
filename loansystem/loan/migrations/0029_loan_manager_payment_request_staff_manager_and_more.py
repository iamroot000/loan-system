# Generated by Django 4.1.7 on 2023-03-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0028_rename_activeloans_borrower_table_active_loans_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.IntegerField(default=0)),
                ('ongoing', models.IntegerField(default=0)),
                ('profit', models.IntegerField(default=0)),
                ('current', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='payment_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('date_request', models.DateField(null=True)),
                ('date_approved', models.DateField(null=True)),
                ('borrower_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=20, null=True, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('date_requested', models.DateField(null=True)),
                ('date_approved', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='loan_payment',
            name='isAudit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loan_payment',
            name='staff',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='loan_table',
            name='staff',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]