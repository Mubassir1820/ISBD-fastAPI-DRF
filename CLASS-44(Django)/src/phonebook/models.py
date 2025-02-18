from django.db import models

class PhoneBook(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    location = models.CharField(max_length=11)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name