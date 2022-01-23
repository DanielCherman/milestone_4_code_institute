from django.urls import path
from .views import Home

app_name = "core"

urlpatterns = [
    path('', Home , name="Home"),
]
