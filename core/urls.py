from django.urls import path

from core.views import ContactCreateView, ContactDetailView, ContactListView, ContactUpdateView

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create", ContactCreateView.as_view(), name="contact_create"),
    path("view/<int:pk>", ContactDetailView.as_view(), name="contact_detail"),
    path("edit/<int:pk>", ContactUpdateView.as_view(), name="contact_edit"),
]
