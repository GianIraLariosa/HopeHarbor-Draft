from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    UserID = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    EmailAddress = models.EmailField()
    USER_TYPES = (
        ('donor', 'Donor'),
        ('beneficiary', 'Beneficiary'),
        ('admin', 'Admin'),
    )
    UserType = models.CharField(max_length=12, choices=USER_TYPES)
    Password = models.CharField(max_length=128)  # Store the hashed password

    class Meta:
        abstract = True
