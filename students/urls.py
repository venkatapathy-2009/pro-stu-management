

from django.urls import path
from .views import home,ad
urlpatterns = [
    path('',home,name='home'),
    path('add/',ad,name='add_st'),

]