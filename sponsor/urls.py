from django.urls import path

from sponsor.viewsets import SponsorViewSet
from sponsor.views import EditSponsorInfoView

urlpatterns = [
    path("list/", SponsorViewSet.as_view({"get": "list"})),
    path(
        "list/<int:id>/",
        SponsorViewSet.as_view({"get": "retrieve", "put": "update"}),
    ),
    path("edit/", EditSponsorInfoView.as_view(), name="edit_sponsor_info"),
]
