from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from notifications.models import Post, Tag
from notifications.models import DeletedPost

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        post = Post.objects.create(title="Django Signals")
        print("Slug:", post.slug)

        user = User.objects.create(username="manoj", email="mn047653@gmail.com")

        tag1 = Tag.objects.create(name="Django")
        tag2 = Tag.objects.create(name="Signals")

        post.tags.add(tag1, tag2)
        post.tags.remove(tag1)

        post.delete()

        print("DeletedPost count:", DeletedPost.objects.count())

        print("\n SQL QUERIES")
        for q in connection.queries:
            print(q["sql"])
