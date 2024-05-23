from ninja import Schema, ModelSchema

from ..models import Employee, Project


class EmployeeIn(ModelSchema):
    project_id: int

    class Meta:
        model = Employee
        exclude = ["id", "project"]


class ProjectIn(ModelSchema):
    class Meta:
        model = Project
        exclude = ["id"]


class ProjectOut(ModelSchema):
    class Meta:
        model = Project
        fields = "__all__"


class EmployeeOut(ModelSchema):
    class Meta:
        model = Employee
        fields = "__all__"
