from ninja import Router
from asyncio import sleep
import time
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


@router.get("/say-sync")
def say_after_sync(request, delay: int, word: str):
    time.sleep(delay)
    return {"saying": word}


@router.get("/say-async")
async def say_after_async(request, delay: int, word: str):
    await sleep(delay)
    return {"saying": word}
