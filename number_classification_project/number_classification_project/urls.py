from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('number_api_app.urls')),  # Make sure this matches your app name
]
