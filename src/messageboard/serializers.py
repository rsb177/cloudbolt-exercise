from rest_framework import serializers

from messageboard.models import Message, Thread, Topic


class ThreadSerializer(serializers.ModelSerializer):
    """
    The Django REST Framework serializer for the Thread class.

    Functions similarly to the ModelForm class.

    https://www.django-rest-framework.org/api-guide/serializers/

    Args:
        serializers.ModelSerializer: Base Django REST Framework Model
            Serializer class.
    """

    class Meta:
        """
        Inherits from the Topic model.

        Exposes all fields.
        """

        model = Thread
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    """
    The Django REST Framework serializer for the Thread class.

    Functions similarly to the ModelForm class.

    https://www.django-rest-framework.org/api-guide/serializers/

    Args:
        serializers.ModelSerializer: Base Django REST Framework Model
            Serializer class.
    """

    class Meta:
        """
        Inherits from the Message model.

        Exposes all fields.
        """

        model = Message
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    """
    The Django REST Framework serializer for the Topic class.

    Functions similarly to the ModelForm class.

    https://www.django-rest-framework.org/api-guide/serializers/

    Args:
        serializers.ModelSerializer: Base Django REST Framework Model
            Serializer class.
    """

    thread_count = serializers.SerializerMethodField()
    message_count = serializers.SerializerMethodField()

    def get_threads(self, topic):
        return topic.threads

    def get_thread_count(self, topic):
        return topic.threads.count()

    def get_message_count(self, topic):
        return Message.objects.filter(thread__topic=topic).count()

    class Meta:
        """
        Inherits from the Topic model.

        Exposes all fields.
        """

        model = Topic
        fields = "__all__"
