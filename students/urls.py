

from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('add/',ad,name='add_st'),
    path('remove/<int:pk>',remove,name='remove'),
    path('edit/<int:pk>',edit,name='edit'),
]