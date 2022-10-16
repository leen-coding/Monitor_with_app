from django.urls import path
from . import views


urlpatterns = [

    path("gethtml/",views.gethtml),

    path("monitor/", views.getmonitor)

]
