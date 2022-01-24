from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Platform İstanbul API Documentation",
        default_version='v1',
        description="An API Documentation for Platform İstanbul",
        terms_of_service="https://www.westerops.com/",
        contact=openapi.Contact(email="info@westerops.com"),
        license=openapi.License(name="westerOps License"),
    ),
    url='https://testapi.platformistanbul.westerops.com/tr/swagger/',
    public=True
)