from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Course, Unit
from .serializers import CourseSerializer, UnitSerializer
from .decorators import validate_course_data, validate_unit_data

# Create your views here.


class ListCreateCheckNameView(generics.ListCreateAPIView):
    """
        GET Chats/
        POST Chats/
        """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        # tag_instance = Chats.objects.get()
        # a_pattern = ChatsSerializer.objects.create(
        #     name=request.data["name"]
        # )
        # Test the chatbot
        res=Course.objects.filter(TAXPAYERPIN=request.data["TAXPAYERPIN"])
        course = res.first()

        s = CourseSerializer(course)
        return Response(
            data=s.data,
            status=status.HTTP_201_CREATED
        )

class ListCreateCourseView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_course_data
    def post(self, request, *args, **kwargs):
        a_tag = Course.objects.create(
            course_code=request.data["course_code"],
            name=request.data["name"],
            period=request.data["period"]

        )
        return Response(
            data=CourseSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_course = self.queryset.get(pk=kwargs["pk"])
            return Response(CourseSerializer(a_course).data)
        except Course.DoesNotExist:
            return Response(
                data={
                    "message": "Course with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_course_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = CourseSerializer()
            updated_course = serializer.update(a_tag, request.data)
            return Response(CourseSerializer(updated_course).data)
        except Course.DoesNotExist:
            return Response(
                data={
                    "message": "Course with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_course = self.queryset.get(pk=kwargs["pk"])
            a_course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response(
                data={
                    "message": "Course with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
class ListCreateUnitView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    @validate_unit_data
    def post(self, request, *args, **kwargs):
        a_tag = Unit.objects.create(
            unit_code=request.data["unit_code"],
            name=request.data["name"],
            period=request.data["period"]

        )
        return Response(
            data=UnitSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )




class getUnitObjects(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    @validate_unit_data
    def post(self, request, *args, **kwargs):

        temp=[]
        for i in Unit.objects.all():
            _unit = UnitSerializer(i).data
            _course = Course.objects.get(id=_unit["course"])
            print(_course)
            if _course:
                course = CourseSerializer(_course).data
            else:
                course: {}
            temp.append(
                {
                    **_unit,
                    "course_object": course
                }
            )
        return Response(
            data=temp,
            status=status.HTTP_201_CREATED
        )



class UnitDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_unit = self.queryset.get(pk=kwargs["pk"])
            return Response(UnitSerializer(a_unit).data)
        except Unit.DoesNotExist:
            return Response(
                data={
                    "message": "Unit with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_unit_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = UnitSerializer()
            updated_unit = serializer.update(a_tag, request.data)
            return Response(UnitSerializer(updated_unit).data)
        except Unit.DoesNotExist:
            return Response(
                data={
                    "message": "Unit with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_unit = self.queryset.get(pk=kwargs["pk"])
            a_unit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Unit.DoesNotExist:
            return Response(
                data={
                    "message": "Unit with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )