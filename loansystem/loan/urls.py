from django.urls import re_path
from . import views

app_name = 'loan'

urlpatterns = [
    re_path(r'^$', views.RequestLoan.as_view(), name='loan'),
]