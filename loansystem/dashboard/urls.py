from django.urls import re_path
from . import views

app_name = 'dashboard'

urlpatterns = [
    re_path(r'^$', views.index.as_view(), name='dashboard'),
    re_path('get-daily-table', views.get_daily_table, name='get-daily-table'),

]