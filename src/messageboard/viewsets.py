from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from messageboard.models import Topic, Thread, Message
from messageboard.serializers import (
    TopicSerializer,
    ThreadSerializer,
    MessageSerializer,
)


class BaseAuthViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TopicViewSet(BaseAuthViewSet):
    """
    Django REST Framework Viewset for Topics.

    Analogous to Django Views. Essentially exposes the TopicSerializer as a
    JSON payload.

    https://www.django-rest-framework.org/api-guide/viewsets/

    Args:
        viewsets.ModelViewSet: Base Django REST Framework ModelViewSet class.
    """

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class ThreadViewSet(BaseAuthViewSet):
    """
    Django REST Framework Viewset for Threads.

    Analogous to Django Views. Essentially exposes the ThreadSerializer as a
    JSON payload.

    https://www.django-rest-framework.org/api-guide/viewsets/

    Args:
        viewsets.ModelViewSet: Base Django REST Framework ModelViewSet class.
    """

    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()


class MessageViewSet(BaseAuthViewSet):
    """
    Django REST Framework Viewset for Messages.

    Analogous to Django Views. Essentially exposes the MessageSerializer as a
    JSON payload.

    https://www.django-rest-framework.org/api-guide/viewsets/

    Args:
        viewsets.ModelViewSet: Base Django REST Framework ModelViewSet class.
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
