from rest_framework import serializers

from ..models import Project, Employee


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(
        source="project",
        queryset=Project.objects.all(),
    )

    class Meta:
        model = Employee
        exclude = ["project"]
