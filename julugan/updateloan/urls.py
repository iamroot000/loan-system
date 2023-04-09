from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="update-loan"),
    re_path('add-loan', views.add_loan, name='add-loan'),
    re_path('get-borrower-details/(?P<loan_id>\d+)', views.get_borrower_details, name='get-borrower-details'),
    re_path('submit-payment-request', views.submit_payment_request, name='submit-payment-request'),
]