# Pytest modules
import pytest

# Django modules
from django.contrib.auth import get_user_model

# DRF modules
from rest_framework.test import APIClient
from rest_framework import status

# Python modules
from decimal import Decimal

# Project modules
from apps.courses.models import Course, Lesson


@pytest.fixture
def api_client():
    """
    Fixture to create API client
    """
    return APIClient()

User = get_user_model()
@pytest.fixture
def create_user(db):
    """
    Fixture to create a user
    """
    def make_user(username="testuser", password="testtest123", **kwargs):
        return User.objects.create_user(
            username=username,
            password=password,
            email=kwargs.get("email", f"{username}@gmail.com"),
            **kwargs
        )
    return make_user

@pytest.fixture
def authenticated_client(api_client, create_user):
    """
    Fixture to create authenticated API client
    """
    user = create_user()
    api_client.force_authenticate(user=user)
    api_client.user = user
    return api_client

@pytest.fixture
def create_course(db):
    """
    Fixture to create a course
    """
    def make_course(owner, **kwargs):
        return Course.objects.create(
            title=kwargs.get("title", "test course"),
            description = kwargs.get("description", "Test course description"),
            owner = owner,
            **kwargs,
        )
    return make_course

@pytest.fixture
def create_lesson(db):
    """
    Fixture to create a course
    """
    def make_lesson(course, **kwargs):
        return Lesson.objects.create(
            course = course,
            title=kwargs.get("title", "test lesson"),
            content = kwargs.get("content", "test lesson content"),
            order = kwargs.get("order", Decimal("0.00000")),
            **kwargs,
        )
    return make_lesson
