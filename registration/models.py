from django.db import models
from django.contrib.auth.models import User


EDUCATION_LEVELS = [
    ("HS","High School Diploma"),
    ("AD","Associate's Degree"),
    ("BD","Bachelor's Degree"),
    ("MD","Master's Degree"),
    ("PHD","Doctorate or PHD")
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    ed_level = models.CharField(choices= EDUCATION_LEVELS, max_length=300, blank = True)

    def __str__(self):
        return str(self.user) + "'s Profile"
