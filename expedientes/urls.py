from django.urls import path
from .views import ExpedienteCreateView, ExpedienteDetailView, ExpedienteListView

urlpatterns = [
    path("", ExpedienteListView.as_view(), name="expediente_list"),
    path("nuevo/", ExpedienteCreateView.as_view(), name="expediente_create"),
    path("<int:pk>/", ExpedienteDetailView.as_view(), name="expediente_detail"),
]
