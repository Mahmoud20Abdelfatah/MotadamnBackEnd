from django.urls import path
from . import views


app_name ='dss_box'

urlpatterns = [
        path('',views.dss_box),
        path('dss_box',views.dss_box),
    ]
