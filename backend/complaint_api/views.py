from rest_framework import generics
from complaint.models import Complaint
from .serializers import ComplaintSerializer


class ComplaintList(generics.ListCreateAPIView):
    queryset = Complaint.complaintobjects.all()
    serializer_class = ComplaintSerializer
    pass

class ComplaintDetail(generics.RetrieveDestroyAPIView):
    pass