from django.db import models

class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ('fanart', 'Fanart'),
        ('original', 'Original'),
        ('sketch', 'Sketch'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='artworks/')
    date = models.DateTimeField(auto_now_add=True)

