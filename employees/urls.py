from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
urlpatterns = [
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
]