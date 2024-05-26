from django import forms

from core.models import ContactPhone


class ContactPhoneForm(forms.ModelForm):
    class Meta:
        model = ContactPhone
        exclude = ["contact"]


ContactPhoneFormset = forms.modelformset_factory(ContactPhone, form=ContactPhoneForm, extra=1)
