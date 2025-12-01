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
class TestLessonList:
    def test_list_lesson_ok(self, auth_client, course):
        Lesson.objects.create(course=course, title="L2", order=1)
        Lesson.objects.create(course=course, title="L3", order=2)

        res = auth_client.get(f"api/v1/apps/courses/{course.id}/lessons/")
        assert res.status_code == HTTP_200_OK
        assert len(res.data) == 2





