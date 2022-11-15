from rest_framework import generics
from complaint.models import Complaint
from .serializers import ComplaintSerializer


class ComplaintList(generics.ListCreateAPIView):
    queryset = Complaint.complaintobjects.all()
    serializer_class = ComplaintSerializer
    

class ComplaintDetail(generics.RetrieveDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer