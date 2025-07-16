from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='myapp/index.html'), name='index'),
]
