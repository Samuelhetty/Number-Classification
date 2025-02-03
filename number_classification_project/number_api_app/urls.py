from django.urls import path
from .views import ClassifyNumberView

urlpatterns = [
    path('api/classify-number/', ClassifyNumberView.as_view(), name='classify_number'),
]
