from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('process_money', views.money),
    path('refresh', views.refresh),
]