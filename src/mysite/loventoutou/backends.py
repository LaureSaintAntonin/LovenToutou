from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, mail_owner=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=mail_owner)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None