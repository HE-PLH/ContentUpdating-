from django.urls import path
from .views import ListCreateCourseView, CourseDetailView,ListCreateCheckNameView, ListCreateUnitView, UnitDetailView, getUnitObjects


urlpatterns = [
    path('course/', ListCreateCourseView.as_view(), name="Course-list-create"),
    path('unit/', ListCreateUnitView.as_view(), name="Unit-list-create"),
    path('get-units/', getUnitObjects.as_view(), name="get-Unit-list-create"),
    path('check_name/', ListCreateCheckNameView.as_view(), name="checkname-list-view"),
    path('course/<int:pk>/', CourseDetailView.as_view(), name="Course-detail"),
    path('unit/<int:pk>/', UnitDetailView.as_view(), name="Unit-detail"),
]
