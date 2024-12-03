from django.urls import path
from .views import administrator_page

urlpatterns = [
    path('', administrator_page)
]
