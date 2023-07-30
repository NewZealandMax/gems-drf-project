from django.urls import path

from api.views import CustomerAPIView

CLIENTS_URL = 'clients/'

app_name = 'api'

urlpatterns = [
    path(CLIENTS_URL, CustomerAPIView.as_view()),
]
