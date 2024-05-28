from ninja import NinjaAPI

from django.core.exceptions import ValidationError
from projects.ninja.api import router as projects_router

api = NinjaAPI()


@api.exception_handler(ValidationError)
def custom_validation_errors(request, exc):
    return api.create_response(request, exc.message_dict, status=422)


api.add_router("", projects_router)
