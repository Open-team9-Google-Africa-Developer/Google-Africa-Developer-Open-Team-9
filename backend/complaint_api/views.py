from rest_framework import generics
from complaint.models import Complaint
from .serializers import ComplaintSerializer
from rest_framework import SAFE_METHODS, BasePermission

class ComplaintUserWritePermission(BasePermission):
    message = 'Editing Complaint is restricted to author only.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.complainant == request.user

class ComplaintList(generics.ListCreateAPIView):
    queryset = Complaint.complaintobjects.all()
    serializer_class = ComplaintSerializer
    

class ComplaintDetail(generics.RetrieveUpdateDestroyAPIView, ComplaintUserWritePermission):
    permission_classes = [ComplaintUserWritePermission]
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer