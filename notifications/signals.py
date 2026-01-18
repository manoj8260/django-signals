from django.db.models.signals import pre_save, post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from .models import DeletedPost, Post


# Automatic Slug Generation
@receiver(pre_save, sender=Post)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug and  instance.title:
        title =instance.title
        instance.slug = slugify(title)


# User Welcome Notification
def send_welcome_email(email):
    print(f"Welcome email sent to {email}")

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user_email=instance.email
        send_welcome_email(user_email)


# Pre-Deletion Backup
@receiver(pre_delete, sender=Post)
def backup_post(sender, instance, **kwargs):
    DeletedPost.objects.create(
        title=instance.title,
        slug=instance.slug,
        deleted_at=timezone.now()
    )


# Many to Many Change Tracking
@receiver(m2m_changed, sender=Post.tags.through)
def track_tag_changes(sender, instance, action, pk_set, **kwargs):
    if action == "pre_add":
        print(f"[{timezone.now()}] PRE_ADD {pk_set} on {instance}")
    elif action == "post_remove":
        print(f"[{timezone.now()}] POST_REMOVE {pk_set} on {instance}")
