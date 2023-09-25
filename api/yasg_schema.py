from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="File Management System",
        default_version='v1',
        description="File Management System using DRF",
        terms_of_service="facebook.com",
        contact=openapi.Contact(email="cjcasol22@gmail.com"),
        license=openapi.License(name="BSD Lisence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)