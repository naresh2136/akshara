from django.urls import path
from crud.views import *


urlpatterns = [
    path('enter_timesheet/', enter_timesheet),
    path('show_timesheet/', show_timesheet),
    path('delete/<int:id>/', delete),
    path('update/<int:id>/', update),
    path('test/', test),
]
