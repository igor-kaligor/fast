from django.conf.urls import include
from django.urls import path
urlpatterns = [
    path(r'api/', include('tutorials.urls')),
]
