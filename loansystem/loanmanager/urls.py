from django.urls import re_path
from . import views

app_name = 'loanmanager'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='loanmanager'),
    re_path('get-loan-table', views.get_loan_table, name='get-loan-table'),
    # re_path('get-request-table', views.get_request_table, name='get-request-table'),
    re_path('add-loan', views.add_loan, name='add-loan'),
    re_path('get-borrower-details/(?P<loan_id>\d+)', views.get_borrower_details, name='get-borrower-details'),
    # re_path('approve-loan', views.approve_loan, name='approve-loan'),
    # re_path('decline-loan',views.decline_loan, name='decline-loan'),
    re_path('submit-payment-request', views.submit_payment_request, name='submit-payment-request'),
]