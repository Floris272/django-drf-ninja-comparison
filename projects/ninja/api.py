from typing import List

from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404
from ninja import Router

from .schemas import EmployeeIn, EmployeeOut, ProjectIn, ProjectOut
from ..models import Project, Employee

router = Router()


@router.get("/projects/{project_id}", response=ProjectOut)
def get_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    return project


@router.get("/projects", response=List[ProjectOut])
def list_projects(request):
    qs = Project.objects.all()
    return qs


@router.post("/projects", response=ProjectOut)
def create_project(request, payload: ProjectIn):
    payload_dict = payload.dict()
    project = Project(**payload_dict)
    project.save()
    return project


@router.get("/aprojects/{project_id}", response=ProjectOut)
async def aget_project(request, project_id: int):
    project = await sync_to_async(get_object_or_404)(Project, id=project_id)
    return project


@router.get("/aprojects", response=List[ProjectOut])
async def alist_projects(request):
    qs = await sync_to_async(list)(Project.objects.all())
    return qs


@router.post("/aprojects", response=ProjectOut)
async def acreate_project(request, payload: ProjectIn):
    payload_dict = payload.dict()
    project = Project(**payload_dict)
    await project.asave()
    return project


@router.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee


@router.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs


@router.post("/employees", response=EmployeeOut)
def create_employee(request, payload: EmployeeIn):
    employee = Employee(**payload.dict())
    employee.full_clean()
    employee.save()
    return employee


@router.delete("/employees/{employee_id}", response={204: None})
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return 204, None


@router.get("/aemployees/{employee_id}", response=ProjectOut)
async def aget_employee(request, employee_id: int):
    employee = await sync_to_async(get_object_or_404)(Employee, id=employee_id)
    return employee


@router.get("/aemployees", response=List[EmployeeOut])
async def alist_employees(request):
    qs = await sync_to_async(list)(Employee.objects.all())
    return qs


@router.post("/aemployees", response=EmployeeOut)
async def acreate_employee(request, payload: EmployeeIn):
    employee = Employee(**payload.dict())
    await sync_to_async(employee.full_clean)()
    await employee.asave()
    return employee


@router.delete("/aemployees/{employee_id}", response={204: None})
async def adelete_employee(request, employee_id: int):
    employee = await sync_to_async(get_object_or_404)(Employee, id=employee_id)
    await employee.adelete()
    return 204, None


@router.post("/restart", response={204: None})
def restart(request):
    if not Project.objects.filter(id=1).exists():
        Project.objects.create(id=1, name="abc", number=20)
    Employee.objects.all().delete()
    return 204, None
