from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Topic, Content
from .serializers import TopicSerializer, ContentSerializer
from .decorators import validate_topic_data, validate_content_data

# Create your views here.


class ListCreateCheckNameView(generics.ListCreateAPIView):
    """
        GET Chats/
        POST Chats/
        """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        # tag_instance = Chats.objects.get()
        # a_pattern = ChatsSerializer.objects.create(
        #     name=request.data["name"]
        # )
        # Test the chatbot
        res=Topic.objects.filter(TAXPAYERPIN=request.data["TAXPAYERPIN"])
        topic = res.first()

        s = TopicSerializer(topic)
        return Response(
            data=s.data,
            status=status.HTTP_201_CREATED
        )

class ListCreateTopicView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_topic_data
    def post(self, request, *args, **kwargs):
        a_tag = Topic.objects.create(
            topic_code=request.data["topic_code"],
            name=request.data["name"],
            period=request.data["years"],

        )
        return Response(
            data=TopicSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_topic = self.queryset.get(pk=kwargs["pk"])
            return Response(TopicSerializer(a_topic).data)
        except Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_topic_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = TopicSerializer()
            updated_topic = serializer.update(a_tag, request.data)
            return Response(TopicSerializer(updated_topic).data)
        except Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_topic = self.queryset.get(pk=kwargs["pk"])
            a_topic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
            

class ListCreateContentView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_content_data
    def post(self, request, *args, **kwargs):
        a_tag = Content.objects.create(
            topic_code=request.data["topic_code"],
            name=request.data["name"],
            period=request.data["years"],

        )
        return Response(
            data=ContentSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_topic = self.queryset.get(pk=kwargs["pk"])
            return Response(ContentSerializer(a_topic).data)
        except Content.DoesNotExist:
            return Response(
                data={
                    "message": "Content with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_content_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = ContentSerializer()
            updated_topic = serializer.update(a_tag, request.data)
            return Response(ContentSerializer(updated_topic).data)
        except Content.DoesNotExist:
            return Response(
                data={
                    "message": "Content with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_topic = self.queryset.get(pk=kwargs["pk"])
            a_topic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Content.DoesNotExist:
            return Response(
                data={
                    "message": "Content with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )