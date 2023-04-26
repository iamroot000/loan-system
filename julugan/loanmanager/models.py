import random
from django.db import models

# Create your models here.
class borrower_table(models.Model):

    borrower_id = models.IntegerField(unique=True, editable=False)
    name = models.CharField(max_length=20, null=True, unique=True)
    completed_loans = models.IntegerField(default=0)
    active_loans = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            while True:
                randomNumber = random.randint(100000,999999)
                if not borrower_table.objects.filter(borrower_id=randomNumber).exists():
                    self.borrower_id = randomNumber
                    break
        super().save(*args, **kwargs)
    
    def __str__(self):
            return str(self.name) 
     
class loan_table(models.Model):

    LOAN_TYPES = [
        ('custom', 'Custom'),
        ('daily', 'Daily'),
    ]

    loan_id = models.IntegerField(unique=True, editable=False)
    loan_type = models.CharField(max_length=8, choices=LOAN_TYPES)
    name = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    amount_loan = models.IntegerField(default=0)
    total_days = models.IntegerField(default=0, null=True)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    paid_days = models.IntegerField(default=0, null=True)
    days_left = models.IntegerField(default=0, null=True)
    paid_amount = models.IntegerField(default=0, null=True)
    amount_per_day = models.IntegerField(default=0, null=True)
    amount_left = models.IntegerField(default=0, null=True)
    progress = models.IntegerField(default=0, null=True)
    status = models.CharField(max_length=15,default='incomplete')
    renew_count = models.IntegerField(default=0, null=True)
    loan_profit = models.IntegerField(default=0, null=True)
    staff_profit = models.IntegerField(default=0, null=True) 
    is_approved = models.BooleanField(default=False)
    staff = models.CharField(max_length=20, null=True)

    def save(self, *args, **kwargs):
            if not self.pk:
                while True:
                    randomNumber = random.randint(100000,999999)
                    if not loan_table.objects.filter(loan_id=randomNumber).exists():
                        self.loan_id = randomNumber
                        break
            super().save(*args, **kwargs)

    def __str__(self):
            return str(self.loan_id)

class loan_payment(models.Model):
     
     loan_id = models.ForeignKey(loan_table, on_delete=models.CASCADE)
     dates_to_pay = models.DateField(null=True)
     paid_dates = models.DateField(null=True)
     paid = models.BooleanField(default=False)
     isAudit = models.BooleanField(default=False)
     staff = models.CharField(max_length=20, null=True)

class loan_manager(models.Model):
    total_balance = models.IntegerField(default=0)
    ongoing = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    current = models.IntegerField(default=0)

class staff_manager(models.Model):
    staff_name = models.CharField(max_length=20, null=True, unique=True)
    amount = models.IntegerField(default=0)
    date_requested = models.DateField(null=True)
    date_approved = models.DateField(null=True)

class payment_request(models.Model):
    request_number = models.IntegerField(unique=True, editable=False, null=True)
    staff_name = models.CharField(max_length=20, null=True)
    amount = models.IntegerField(null=True)
    dates_request = models.TextField(max_length=500, null=True)
    date_approved = models.DateField(null=True)
    borrower_name = models.CharField(max_length=20, null=True)
    loan_id = models.IntegerField(null=True)
    request_date = models.DateField(null=True)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
            if not self.pk:
                while True:
                    randomNumber = random.randint(100000,999999)
                    if not payment_request.objects.filter(request_number=randomNumber).exists():
                        self.request_number = randomNumber
                        break
            super().save(*args, **kwargs)

class bank(models.Model):
     total_balance = models.IntegerField(null=True)
     active_loans = models.IntegerField(null=True)
     available_balance = models.IntegerField(null=True)
     active_borrowers = models.IntegerField(null=True)