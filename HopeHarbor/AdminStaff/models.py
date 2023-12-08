from django.db import models
from User.models import User

class AdminStaff(User):
    UserType = models.CharField(
        max_length=12,
        choices=User.USER_TYPES,  # Use choices from User model
        default='admin',  # Set the default to 'donor'
    )

    def __str__(self):
        return f"Admin - {self.Username}"
