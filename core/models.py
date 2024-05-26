from django.db import models


class Contact(models.Model):
    """Contact model."""

    name = models.CharField(max_length=255)
    # add more contact details here

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class ContactPhone(models.Model):
    """Contact phone model."""

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="phones")
    number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact} - {self.phone}"

    class Meta:
        verbose_name = "Contact phone"
        verbose_name_plural = "Contact phones"
