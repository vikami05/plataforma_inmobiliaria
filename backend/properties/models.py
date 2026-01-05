from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'Casa'),
        ('apartment', 'Departamento'),
        ('land', 'Terreno'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
