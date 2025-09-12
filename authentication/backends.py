from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

Client = get_user_model()

class EmailBackend(BaseBackend):
    @staticmethod
    def authenticate(email=None, password=None, **kwargs):
        try:
            client = Client.objects.get(email=email)
        except Client.DoesNotExist:
            return None
        if client.check_password(password):
            return client
        return None

    def get_client(self, client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None
