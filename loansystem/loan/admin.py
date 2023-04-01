from django.contrib import admin
from .models import borrower_table, loan_table, loan_payment, payment_request, staff_manager, loan_manager
# Register your models here.

class BorrowerAdmin(admin.ModelAdmin):
    readonly_fields = ['borrower_id']
    list_display = ['borrower_id','name','active_loans','completed_loans']

class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ['loan_id']
    list_display =['loan_id','name','amount_loan']

class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ['dates_to_pay','paid']

admin.site.register(borrower_table, BorrowerAdmin)
admin.site.register(loan_table, LoanAdmin)
admin.site.register(loan_payment, LoanPaymentAdmin)
admin.site.register(loan_manager)
admin.site.register(staff_manager)
admin.site.register(payment_request)