from django.urls import path, include
from api_v1.views import *

apiRouter = [
    path("get_user_activity", UserDetailsView.as_view(), name="user_activity")
]

urlpatterns = [
    path("v1/", include((apiRouter, "api_v1"), namespace="v1"))
]