from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="loan-manager"),
]