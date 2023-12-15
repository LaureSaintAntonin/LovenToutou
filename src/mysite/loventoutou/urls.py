from django.urls import path
from . import views

# La fonction path() reçoit quatre paramètres,
# dont deux sont obligatoires : route et view, et deux facultatifs : kwargs et name.
urlpatterns = [
	path("", views.index, name="index"),
]