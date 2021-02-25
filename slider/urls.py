from django.urls import path, include
from .views import home, log_out

urlpatterns=[
    path('', home, name='home'),
    path('logout', log_out, name='logout'),
]
