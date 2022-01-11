from django.urls import path
from .views import *

urlpatterns = [
    path("", Movielist),
    path("add/", post_Movie),
    path("update/", update_Movie),
    path("delete/", delete_Movie),
]