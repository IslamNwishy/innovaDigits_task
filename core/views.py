from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core.forms import ContactPhoneFormset
from core.models import Contact, ContactPhone

# Create your views here.


class ContactCreateView(CreateView):
    model = Contact
    template_name = "core/contact_form.html"
    fields = ["name"]
    success_url = reverse_lazy("contact_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if "formset" not in context_data:
            context_data["formset"] = ContactPhoneFormset(queryset=ContactPhone.objects.none())
        return context_data

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        formset = ContactPhoneFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)

        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        with transaction.atomic():
            response = super().form_valid(form)
            instances = formset.save(commit=False)
            for instance in instances:
                instance.contact = self.object
                instance.save()

        return response

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ContactListView(ListView):
    model = Contact
    template_name = "core/contact_list.html"


class ContactDetailView(DetailView):
    model = Contact
    template_name = "core/contact_details.html"


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "core/contact_form.html"
    fields = ["name"]
    success_url = reverse_lazy("contact_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if "formset" not in context_data:
            context_data["formset"] = ContactPhoneFormset(queryset=self.object.phones.all())
        return context_data

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()
        formset = ContactPhoneFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)

        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        with transaction.atomic():
            response = super().form_valid(form)
            instances = formset.save(commit=False)
            for instance in instances:
                instance.contact = self.object
                instance.save()

        return response

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))
