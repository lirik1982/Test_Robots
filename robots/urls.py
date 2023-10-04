from django.urls import path
from .views import RobotView, RobotReports

urlpatterns = [
    path('new', RobotView.as_view(), ),
    path('report', RobotReports.as_view(), name='get_robots', ),
]
