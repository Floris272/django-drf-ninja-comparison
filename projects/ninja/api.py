from ninja import Router
from ..models import Project, Employee
from .schemas import EmployeeIn, EmployeeOut, ProjectIn, ProjectOut

router = Router()


@router.post("/project")
def create_project(request, payload: ProjectIn):
    payload_dict = payload.dict()
    project = Project(**payload_dict)
    project.save()
    return {"id": project.id}


@router.post("/employee")
def create_employee(request, payload: EmployeeIn):
    employee = Employee(**payload.dict())
    employee.full_clean()
    employee.save()
    return {"id": employee.id}
