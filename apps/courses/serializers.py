
# Python modules
from dataclasses import field
from decimal import Decimal
from typing import Required
from xml.dom import ValidationErr
# Project modules
from .models import Course, Lesson
from apps.users.models import CustomUser
# Django REST framework modules
from rest_framework.serializers import (
    Serializer, 
    SerializerMethodField, 
    IntegerField, 
    ValidationError,
)


class UserSerializer(Serializer):
    """
    Serializer for user to show his info
    """
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "phone"]


class LessonSerializer(Serializer):
    """
    Serializer for lesson
    """
    class Meta:
        model = Lesson
        fields = ["id", "course", "title", "content", "indentation", "is_published", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class LessonCreateSerializer(Serializer):
    """
    Serializer for creating lessons
    """
    class Meta:
        model = Lesson
        fields = ["id", "title", "content","created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validate_data):
        course = self.context["course"]
        lessons = Lesson.objects.filter(course=course)
        if lessons.exists():
            min_order = lessons.order_by("order").first()
            new_order = (min_order.order - Decimal("1.00000")) if min_order else Decimal("1.00000")
        else:
            new_order = Decimal(0.00000)
            validate_data["course"] = course
            validate_data["order"] = new_order
            validate_data["indentation"] = 0

            return super().create(validate_data)
        

class CourseSerializer(Serializer):
    """
    Serialzier for course
    """
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "owner"]

    
class CourseCreateSerializer(Serializer):
    """
    Serializer for creating courses
    """
    class Meta:
        model = Course
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
    

class CourseUpdateSerializer(Serializer):
    """
    Serializer for updating courses
    """
    class Meta:
        model = Course
        fields = ["id", "title", "description", "is_active"]


class LessonMoveSerializer(Serializer):
    """
    Serializer for moving lessons
    """
    before_lesson_id = IntegerField(required=False, allow_null=True)

    def validate_befor_lesson_id(self, value):
        if value is not None:
            try:
                lesson = Lesson.objects.get(id=value)
                moving_lesson = self.context["lesson"]
                if lesson.course != moving_lesson.course:
                    raise ValidationError(
                        "Lesson must be in the same course"
                    )
            except Lesson.DoesNotExist:
                raise ValidationError("Lesson doest not exist")
        return value