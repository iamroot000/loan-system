from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="update-loan"),
    re_path('add-loan-daily', views.add_loan_daily, name='add-loan-daily'),
    re_path('add-loan-custom', views.add_loan_custom, name='add-loan-custom'),
    re_path('get-borrower-details/(?P<loan_id>\d+)', views.get_borrower_details, name='get-borrower-details'),
    re_path('submit-payment-request', views.submit_payment_request, name='submit-payment-request'),
    re_path('complete-payment', views.complete_request, name='complete-payment'),
]