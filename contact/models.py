from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Contact(models.Model):
    # Name: Required field
    name = models.CharField(max_length=255, blank=False)

    # Email: Required field with email validation
    email = models.CharField(
        max_length=255,
        validators=[EmailValidator()],
        blank=False
    )

    # Phone: Required field with a basic phone number validation
    phone = models.CharField(
        max_length=255,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )],
        blank=False
    )

    # Location: Optional field with default value
    location = models.CharField(
        max_length=255,
        default="No location"
    )

    # Message: Optional field with default value
    message = models.CharField(
        max_length=255,
        default="No message"
    )
