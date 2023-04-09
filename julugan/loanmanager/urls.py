from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="loan-manager"),
    re_path('approve-loan', views.approve_loan, name='approve-loan'),
    re_path('decline-loan',views.decline_loan, name='decline-loan'),
]