from django.db import models
from datetime import timedelta
from django.utils import timezone
import uuid


def one_week_from_now():
    return timezone.now() + timedelta(weeks=1)

class ProductPhrase(models.TextChoices):
    noPhrase = 'NOPHRASE', 'No phrase'
    custom = 'CUSTOM', 'Custom'
    f1 = 'F1', 'Faça a diferença, inKlua!'
    f2 = 'F2', 'Todos merecem viver grandes experiências'
    f3 = 'F3', '#InklusaoParaTodos'

class ProductPhraseTyphografy(models.TextChoices):
    Standard = "STANDARD", "Standard"
    Braille = "BRAILLE", "Braille"
    Pixelated = "PIXELATED", "Pixelated"

class ProductIcon(models.TextChoices):
    ban = 'BAN', 'Ban'
    ear = 'EAR', 'Ear'
    eye = 'EYE', 'Eye'
    messageCircle = 'MESSAGECIRCLE', 'Message Circle'
    brain = 'BRAIN', 'Brain'
    accessibility = 'ACCESSIBILITY', 'accessibility'
    star = 'STAR', 'Star'
    gamepad = 'GAMEPAD', 'Gamepad'
    gem = 'GEM', 'Gem'
    heart = 'HEART', 'Heart'
    music = 'MUSIC', 'Music'
    # accessibility = 'ACCESSIBILITY', 'Accessibility'
    
class ProductSize(models.TextChoices):
    small = 'SMALL', 'Small',
    medium = 'MEDIUM', 'Medium'
    big = 'BIG', 'Big'

class ProductColor(models.TextChoices):
    red = 'RED', 'Red'
    green = 'GREEN', 'Green'
    orange = 'ORANGE', 'Orange'
    blue = 'BLUE', 'Blue'
    purple = 'PURPLE', 'Purple'
    black = 'BLACK', 'Black'


class ProductName(models.TextChoices):
    inkluabottle = 'INKLUABOTTLE', 'InkluaBottle'
    inkluabracelet = 'INKLUABRACELET', 'Bracelet'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, choices=ProductName.choices)
    color = models.CharField(max_length=255, choices=ProductColor.choices)
    size = models.CharField(max_length=255, choices=ProductSize.choices)
    icon = models.CharField(max_length=255, choices=ProductIcon.choices, default='NoIcon')
    typography = models.CharField(max_length=255, choices=ProductPhraseTyphografy.choices, default='Standard')
    phrase = models.CharField(max_length=255, choices=ProductPhrase.choices, default='noPhrase')
    client = models.ForeignKey(
        "clients.ClientProfile", 
        on_delete=models.CASCADE, 
        related_name="product")

    def __str__(self):
        return f"Produto {self.name} do cliente {self.client}"
    
class SaleProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    queue_order_id = models.CharField(max_length=255, editable=False)
    sale_date = models.DateTimeField(auto_now_add=True)
    delivery_forecast = models.DateTimeField(default=one_week_from_now)
    status = models.CharField(max_length=100, null=False)   
    status_start_date = models.DateTimeField(null=True)
    status_finished_date = models.DateTimeField(null=True)
    preparation = models.DateTimeField(null=True)
    ready = models.DateTimeField(null=True)
    delivered = models.DateTimeField(null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    position_table = models.IntegerField(null=True)
    client = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name="sale_product")

class NotificationStore(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    sale = models.OneToOneField(SaleProduct, on_delete=models.CASCADE, related_name="notification")
    # client = models.ForeignKey(
    #     "clients.ClientProfile",
    #     on_delete=models.CASCADE,
    #     related_name="notification-store")

class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    product = models.CharField(max_length=100, choices=ProductName.choices),
    colum = models.CharField(max_length=5)
    floor = models.CharField(max_length=5),
    position = models.CharField(max_length=10)
    status = models.CharField(max_length=100),
    quantity_min = models.IntegerField(null=True),
    quantity = models.IntegerField(null=True)
