from django.test import Client, TestCase
from django.urls.base import reverse

from messageboard.factories import (
    MessageFactory,
    ThreadFactory,
    TopicFactory,
    UserFactory,
)


class UnauthTestCases(TestCase):
    """Automated tests for verifying appropriate permissions"""

    def setUp(self):
        self.author = UserFactory()
        self.topic = TopicFactory()
        self.thread = ThreadFactory(topic=self.topic, author=self.author)
        self.message = MessageFactory(thread=self.thread, author=self.author)

    def test_login_requried_to_post_thread(self):
        response = self.client.get(
            reverse("threads", kwargs={"topic_slug": self.topic.slug})
        )
        self.assertNotContains(response, 'role="button">New thread</a>')

        response = self.client.get(
            reverse("new_thread", kwargs={"topic_slug": self.topic.slug})
        )
        self.assertEquals(response.status_code, 302)

    def test_login_requried_to_post_message(self):
        url_params = {"topic_slug": self.topic.slug, "thread_id": self.thread.id}
        response = self.client.get(reverse("messages", kwargs=url_params))
        self.assertNotContains(response, 'role="button">New message</a>')

        response = self.client.get(reverse("new_message", kwargs=url_params))
        self.assertEquals(response.status_code, 302)


class AuthTestCases(TestCase):
    """Automated tests for verifying appropriate permissions"""

    def setUp(self):
        self.author = UserFactory()
        self.not_author = UserFactory()
        self.topic = TopicFactory()
        self.thread = ThreadFactory(topic=self.topic, author=self.author)
        self.message = MessageFactory(thread=self.thread, author=self.author)

        self.client = Client()
        self.client.force_login(user=self.not_author)

    def test_login_requried_to_post_thread(self):
        response = self.client.get(
            reverse("threads", kwargs={"topic_slug": self.topic.slug})
        )
        self.assertContains(response, 'role="button">New thread</a>')

        response = self.client.get(
            reverse("new_thread", kwargs={"topic_slug": self.topic.slug})
        )
        self.assertEquals(response.status_code, 200)

    def test_login_requried_to_post_message(self):
        url_params = {"topic_slug": self.topic.slug, "thread_id": self.thread.id}
        response = self.client.get(reverse("messages", kwargs=url_params))
        self.assertContains(response, 'role="button">New message</a>')

        response = self.client.get(reverse("new_message", kwargs=url_params))
        self.assertEquals(response.status_code, 200)
