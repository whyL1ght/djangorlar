# Django modules
from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator

# Project modules
from apps.users.models import CustomUser
from apps.abstracts.models import AbstractSoftDeletableModel


class Course(AbstractSoftDeletableModel):
    """
    Model representing course in this project
    """
    TITLE_NAME_LENGHT = 200

    title = models.CharField(max_length=TITLE_NAME_LENGHT)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owned_courses")

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title


class Lesson(AbstractSoftDeletableModel):
    """
    Model representing lesson in this project
    """
    TITLE_NAME_LENGHT = 200

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal(0))
    indentation = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"



