from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

CustomUser = get_user_model()

class CustomBackend(BaseBackend):
    def authenticate(email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
