from django.urls import path
from .views import LessonList, LessonDetail


urlpatterns = [
    path('', LessonList.as_view(), name='lesson_list'),
    path('detail/<int:pk>/', LessonDetail.as_view(), name='lesson_detail'),
]