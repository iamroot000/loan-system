from django.urls import re_path
from . import views

app_name = 'systemmanager'

urlpatterns = [
    re_path(r'^$', views.ManageSystem.as_view(), name='loan'),
]