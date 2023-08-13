from django.urls import path

from .views import ListCreateTopicView, TopicDetailView, ListCreateCheckNameView, ListCreateContentView, \
    ContentDetailView

urlpatterns = [
    path('topic/', ListCreateTopicView.as_view(), name="Topic-list-create"),
    path('content/', ListCreateContentView.as_view(), name="Content-list-create"),
    path('check_name/', ListCreateCheckNameView.as_view(), name="checkname-list-view"),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name="Topic-detail"),
    path('content/<int:pk>/', ContentDetailView.as_view(), name="Content-detail"),
]
