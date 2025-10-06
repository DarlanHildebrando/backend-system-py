from django.db import models
import uuid

class ProductIcon(models.TextChoices):
    noIcon = 'NOICON', 'No Icon'
    ear = 'EAR', 'Ear'
    eye = 'EYE', 'Eye'
    speechBubble = 'SPEECHBUBBLE', 'Speech Bubble'
    brain = 'BRAIN', 'Brain'
    wheelchair = 'WHEELCHAIR', 'Wheelchair'
    star = 'STAR', 'Star'
    gamepad = 'GAMEPAD', 'Gamepad'
    diamond = 'DIAMOND', 'Diamond'
    heart = 'HEART', 'Heart'
    music = 'MUSIC', 'Music'
    accessibility = 'ACCESSIBILITY', 'Accessibility'
    
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
    bracelet = 'BRACELET', 'Bracelet'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, choices=ProductName.choices)
    color = models.CharField(max_length=255, choices=ProductColor.choices)
    size = models.CharField(max_length=255, choices=ProductSize.choices)
    icon = models.CharField(max_length=255, choices=ProductIcon.choices, default='NoIcon')
    client = models.ForeignKey(
        "clients.ClientProfile", 
        on_delete=models.CASCADE, 
        related_name="product")

    def __str__(self):
        return f"Produto {self.name} do cliente {self.client.nome}"