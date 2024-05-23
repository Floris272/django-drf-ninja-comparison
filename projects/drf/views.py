from rest_framework import viewsets

from .serializers import ProjectSerializer, EmployeeSerializer
from ..models import Project, Employee


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
