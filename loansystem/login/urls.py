from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index.as_view(), name="login"),
]