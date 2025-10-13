# Python modules
from typing import Any

# Django modules
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Project modules
from apps.abstracts.models import AbstractSoftDeletableModel


class Project(AbstractSoftDeletableModel):
    """
    Represent project db model
    """

    name_max_len = 100

    name = models.CharField(max_length=name_max_len)
    description = models.TextField(blank=True)
    is_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_projects")
    users = models.ManyToManyField(to=User, blank=True, related_name="joined_project")

    def __str__(self):
        return self.name


class Tasks(AbstractSoftDeletableModel):
    """
    Represent tasks db model
    """

    STATUS_CHOICES = [
        ("appointed", "Appointed"),
        ("in_progress", "In_progress"),
        ("done", "Done"),
    ]
    name_max_len = 100

    name = models.CharField(max_length=name_max_len)
    deadline = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    status = models.TextField(choices=STATUS_CHOICES)
    assignees = models.ManyToManyField(
        to=User, 
        through="UserTasks",
        through_fields=("task", "user"),
        blank=True
    )

    def __str__(self):
        return self.name


class UserTasks(AbstractSoftDeletableModel):
    """
    Represent users task in db model
    """
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="user_task")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("task", "user"),
                name="unique_task_user",
            )
        ]






