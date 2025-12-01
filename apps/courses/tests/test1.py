# Pytest modules
import pytest

# Django modules
from django.contrib.auth import get_user_model

# DRF modules
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

# Python modules
from decimal import Decimal

from courses.models import Course, Lesson

@pytest.mark.django_db
class TestJWT:
    def test_token_ok(self, client, user):
        res = client.post("api/token", {"username": "test4", "password": "testtest44"})
        assert res.status_code == HTTP_200_OK
        assert "access" in res.data

    def test_token_wrong(self, client, user):
        res = client.post("api/token", {"username": "test4", "password": "wrongpass"})
        assert res.status_code == HTTP_401_UNAUTHORIZED