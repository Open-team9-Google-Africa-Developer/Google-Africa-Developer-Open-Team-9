from django.urls import path
from django.views.generic import TemplateView

app_name = 'complaint'

urlpatterns = [
    path('', TemplateView.as_view(template_name='complaint/index.html')),
]
