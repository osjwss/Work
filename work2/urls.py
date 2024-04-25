from django.urls import path
from .views import ManufacturerList
urlpatterns = [
    path("search/",view=ManufacturerList.as_view())
]