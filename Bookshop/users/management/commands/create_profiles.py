from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUser = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_without_profile = AuthUser.objects.filter(profile=None)
        for user in users_without_profile:
            Profile.objects.create(user=user)
