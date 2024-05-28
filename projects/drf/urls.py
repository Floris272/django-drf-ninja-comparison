from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, EmployeeViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

router = DefaultRouter(trailing_slash=False)
router.register("projects", ProjectViewSet)
router.register("employees", EmployeeViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path("docs", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
