# Pytest modules
import pytest

# Django modules
from django.contrib.auth import get_user_model

# DRF modules
from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED, 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_403_FORBIDDEN,
    HTTP_204_NO_CONTENT,
)

# Python modules
from decimal import Decimal

# Project modules
from apps.courses.models import Course, Lesson


@pytest.mark.django_db
class TestCourseListCreate:
    def test_list_requires_auth(self, client):
        res = client.get("api/v1/apps/courses/")
        assert res.status_code == HTTP_401_UNAUTHORIZED

    def test_list_ok(self, auth_client, user):
        Course.objects.create(title="C1", owner=user)
        Course.objects.create(title="C2", owner=user)

        res = auth_client.get("api/v1/apps/courses/")
        assert res.status_code == HTTP_200_OK
        assert len(res.data) == 2

    def test_create_ok(self,auth_client):
        res = auth_client.post("api/v1/apps/courses/", {
            "title": "Djangorlar project",
            "description": "test description",
        })
        assert res.status_code == HTTP_201_CREATED

@pytest.mark.django_db
class TestCourseRetrieveUpdate:
    def test_retrieve_ok(self, auth_client, course):
        res = auth_client.get(f"api/v1/apps/courses/{course.id}/")
        assert res.status_code == HTTP_200_OK

    def test_update_owner_ok(self, auth_client, course):
        res = auth_client.put(f"api/v1/apps/courses/{course.id}/",{
            "title": "Updated",
            "description": "Updated",
            "is_active": False
        })
        assert res.status_code == HTTP_200_OK

    def test_update_not_owner(self, auth_client):
        other = User.objects.create_user("other", password="other123456")
        c = Course.objects.create(titile="something", owner=other)

        res = auth_client.put(f"api/v1/apps/courses/{c.id}/", {"title": "something2"})
        assert res.status_code == HTTP_403_FORBIDDEN

@pytest.mark.django_db
class TestCourseDelete:
    def test_delete_ok(self, auth_client, course):
        res = auth_client.delete(f"api/v1/apps/courses/{course.id}/")
        assert res.status_code == HTTP_204_NO_CONTENT
    
    def test_delete_not_owner(self, auth_client):
        other = User.objects.create_user("other3", password="124332other")
        c = Course.objects.create(title="other5", owner = other)

        res = auth_client.delete(f"api/v1/apps/courses/{c.id}")
        assert res.status_code == HTTP_403_FORBIDDEN

