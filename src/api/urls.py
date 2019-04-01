from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from . import views 

API_TITLE = 'Greenfield REST API'
API_DESCRIPTION = 'REST API for exploratory analysis'

schema_view = get_schema_view(title=API_TITLE)

router = DefaultRouter()
router.register(r'widgets', views.WidgetViewSet)

urlpatterns = [
        path('schema/', schema_view),
        path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
        path('', include(router.urls)),
]
