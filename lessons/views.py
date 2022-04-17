from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.response import Response

from .models import Lesson
from .serializers import LessonSerializer


class LessonList(generics.GenericAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.initial_data['student'] = request.user.pk  # Todo 'set user default'
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LessonDetail(generics.GenericAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        lesson = self.get_object()
        return Response(self.serializer_class(lesson).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        lesson = self.get_object()
        serializer = self.serializer_class(instance=lesson, data=request.data)
        serializer.initial_data['student'] = request.user.pk
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        lesson = self.get_object()
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)