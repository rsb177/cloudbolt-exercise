import random

from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from messageboard.factories import (
    TopicFactory,
    ThreadFactory,
    MessageFactory,
    UserFactory,
)
from messageboard.models import Topic, Thread, Message

User = get_user_model()


class Command(BaseCommand):
    help = "Seed example data into the database."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Deleting old data...")
        models = [Topic, Thread, Message, User]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Generating users...")
        users = []
        for i in range(50):
            user = UserFactory()
            user.save()
            users.append(user)

        self.stdout.write("Generating messageboard models...")
        for i in range(5):
            topic = TopicFactory()

            num_threads = random.randint(10, 50)
            for _ in range(num_threads):
                thread = ThreadFactory(
                    topic=topic, author=random.choice(User.objects.all())
                )

                num_messages = random.randint(25, 100)
                for _ in range(num_messages):
                    MessageFactory(
                        thread=thread, author=random.choice(User.objects.all())
                    )
            self.stdout.write(f"Topic generated: {topic}")

        return
