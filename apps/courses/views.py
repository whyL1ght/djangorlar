from decimal import Decimal
from rest_framework.viewsets import ViewSet
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_204_NO_CONTENT,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404, render

from .models import Course, Lesson
from .serializers import (
    CourseSerializer,
    CourseCreateSerializer,
    CourseUpdateSerializer,
    LessonSerializer,
    LessonMoveSerializer,
    LessonCreateSerializer,
)
from .permissions import IsCourseOwner
from apps.courses import serializers

class CourseViewSet(ViewSet):
    """
    ViewSet for course CRUD operations
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        List all courses
        """
        queryset = Course.objects.all()
        is_active = request.query_params.get("is_active", None)
        if is_active is not None:
            is_active_bool = is_active.lower()
            queryset = queryset.filter(is_active=is_active_bool)

        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        Create a new course
        """
        serializer = CourseCreateSerializer(
            data = request.data,
            context = {"request": request}
        )
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                CourseSerializer(course).data,
                status = HTTP_201_CREATED
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """
        Get a single course by ID
        """
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """
        Update a course
        """
        course = get_object_or_404(Course, pk=pk)
        if course.owner != request.user:
            return Response(
                {"detail": "You don't have permission to update this course"},
                status = HTTP_403_FORBIDDEN
            )
        
        serializer = CourseUpdateSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CourseSerializer(course).data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
        Delete a course
        """
        course = get_object_or_404(Course, pk=pk)
        if course.owner != request.user:
            return Response(
                {"detail": "You don't have permission to delete this course"},
                status = HTTP_403_FORBIDDEN
            )
        course.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        """
        Activate a course
        """
        course = get_object_or_404(Course, pk=pk)
        if course.owner != request.user:
            return Response(
                {"detail": "You don't have permission to activate this course"},
                status = HTTP_403_FORBIDDEN
            )
        if course.is_active:
            return Response(
                {"detail": "Course is already active"},
                status=HTTP_400_BAD_REQUEST
            )
        course.is_active = True
        course.save()
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def deactivate(self, request, pk=None):
        """
        Deactivate a course
        """
        course = get_object_or_404(Course, pk=pk)
        if course.owner != request.user:
            return Response(
                {"detail": "You don't have permission to activate this course"},
                status = HTTP_403_FORBIDDEN
        )
        course.is_active = False
        course.save()
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    @action(detail=True, methods=["get"])
    def lessons(self, request, pk=None):
        """
        List all lessons of a course
        """
        course = get_object_or_404(Course, pk=pk)
        lessons = course.lessons.all() # type: ignore[attr-defined]
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    
class LessonViewSet(ViewSet):
    """
    View set for CRUD lessons operations
    """
    permission_classes = [IsAuthenticated]

    def create(self,request):
        """
        Create a new lesson
        """
        course_id = request.data.get("course_id")
        if not course_id:
            return Response(
                {"detail": "course id is required"},
                status=HTTP_400_BAD_REQUEST
            )
        course = get_object_or_404(Course, pk=course_id)
        if course.owner != request.owner:
            return Response(
                {"detail:" "You don't have permission to create lesson"},
                status=HTTP_403_FORBIDDEN
            )
        serializer = LessonCreateSerializer(data=request.data, context={"course": course})
        if serializer.is_valid():
            lesson = serializer.save()
            return Response(
                LessonSerializer(lesson).data,
                status=HTTP_201_CREATED
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["put"])
    def move(self, request, pk=None):
        """
        Move a lesson
        """
        lesson = get_object_or_404(Lesson,pk=pk)
        if lesson.course.owner != request.owner:
            return Response(
                {"detail:" "You don't have permission to move lesson"},
                status=HTTP_403_FORBIDDEN
            )
        serializer = LessonMoveSerializer(data=request.data, context={"lesson": lesson})
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        before_lesson_id = serializer.validated_data.get("before_lesson_id") # type: ignore[reportOptionalMemberAccess]
        if before_lesson_id is None:
            lessons = Lesson.objects.filter(course=lesson.course)
            if lessons.exists():
                min_order = lessons.order_by("order").first()
                new_order = (min_order.order - Decimal("1.00000")) if min_order else Decimal("1.00000")
            else:
                new_order = Decimal(0.00000)
            new_indentation = 0
        else:
            before_lesson = get_object_or_404(Lesson, pk=before_lesson_id)
            previous_lesson = Lesson.objects.filter(
                course = lesson.course,
                order__lt=before_lesson.order,
            ).order_by("-order").first()
            
            if previous_lesson:
                new_order = (previous_lesson.order + before_lesson.order) / 2
                new_indentation = previous_lesson.indentation
            else:
                new_order = before_lesson.order - Decimal("1.00000")
                new_indentation = 0

        lesson.order = new_order
        lesson.indentation = new_indentation
        lesson.save()

        return Response({
            "order": str(lesson.order),
             "indentation": lesson.indentation
             })
    
    def destroy(self, request, pk=None):
        """
        Delete a lesson
        """
        lesson = get_object_or_404(Lesson, pk=pk)
        
        if lesson.course.owner != request.owner:
            return Response(
                {"detail:" "You don't have permission to move lesson"},
                status=HTTP_403_FORBIDDEN
            )
        lesson.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        """
        Publish a lesson
        """
        lesson = get_object_or_404(Lesson, pk=pk)

        if lesson.course.owner != request.owner:
            return Response(
                {"detail:" "You don't have permission to move lesson"},
                status=HTTP_403_FORBIDDEN
            )
        lesson.is_published = True
        lesson.save()
        serialzier = LessonSerializer(lesson)
        return Response(serialzier.data)
    
    @action(detail=True, methods=["post"])
    def unpublish(self, request, pk=None):
        """
        Unpublish a lesson
        """
        lesson = get_object_or_404(Lesson, pk=pk)

        if lesson.course.owner != request.owner:
            return Response(
                {"detail:" "You don't have permission to move lesson"},
                status=HTTP_403_FORBIDDEN
            )
        lesson.is_published = False
        lesson.save()
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
    
