from django.contrib import admin
from django.urls import path
from .views import car_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/car/', csrf_exempt(car_view), name='car')
]