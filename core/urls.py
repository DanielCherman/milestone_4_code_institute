from django.urls import path
from .views import ContactUsView, Home

app_name = "core"

urlpatterns = [
    path('', Home , name="Home"),
    path('contact-us/', ContactUsView, name="Contact"),
]
