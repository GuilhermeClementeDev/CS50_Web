from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("guizin", views.guizin, name="guizin"),
	path("<str:name>", views.greet, name="greet")
]
