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
        ('monthly', 'Monthly'),
        ('daily', 'Daily'),
    ]

    # def get_borrower_choices():
    #     borrowers = borrowers = borrower_table.objects.all()
    #     choices = [(borrower.name, borrower.name) for borrower in borrowers]
    #     return choices

    loan_id = models.IntegerField(unique=True, editable=False)
    loan_type = models.CharField(max_length=8, choices=LOAN_TYPES)
    name = models.CharField(max_length=20, null=True, unique=True)
    # name = models.ForeignKey(borrower_table, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    amount_loan = models.IntegerField()
    total_days = models.IntegerField()
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    paid_days = models.IntegerField(default=0)
    days_left = models.IntegerField(default=0)
    paid_amount = models.IntegerField(default=0)
    amount_per_day = models.IntegerField()
    amount_left = models.IntegerField()
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=15,default='incomplete')
    renew_count = models.IntegerField(default=0)
    loan_profit = models.IntegerField(default=0)
    tata_profit = models.IntegerField(default=0) 
    is_approved = models.BooleanField(default=False)


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
