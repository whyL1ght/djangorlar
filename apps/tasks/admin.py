# Django modules
from django.contrib import admin

# Project modules
from .models import(
    Project,
    Tasks,
    UserTasks
)

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    """
    Project admin registration class
    """
    list_display=("name", "description", "is_author", "created_at", "updated_at",)
    search_fields = ("name", "is_author")
    readonly_fields = ("created_at", "updated_at",)
    list_filter = ("name", "created_at",)
    ordering = ("-created_at",)

@admin.register(Tasks)
class AdminTask(admin.ModelAdmin):
    """
    Task admin registration class
    """
    list_display = ("name", "deadline", "status", "created_at", "updated_at",)
    search_fields = ("name", "status",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(UserTasks)
class AdminUserTasks(admin.ModelAdmin):
    """
    User Tasks registration class
    """
    list_display = ("user", "task",)
    list_filter = ("user", "task",)
    search_fields = ("user__name", "task__name",)

