from django.urls import path
from .views import ComplaintList, ComplaintDetail

app_name = 'complaint_api'

urlpatterns = [
    path('complaint/<int:pk>/', ComplaintDetail.as_view(), name='complaintdetail'),
    path('complaints', ComplaintList.as_view(), name='complaintlist'),
       
]
