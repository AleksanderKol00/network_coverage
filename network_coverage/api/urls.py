from django.urls import path

from api import views

urlpatterns = [
    path("", views.NetworkCoverageView.as_view(), name="network_coverage"),
]
