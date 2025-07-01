from django.db import models

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('image1', 'Image1'),
        ('image2', 'Image2'),
        ('image3', 'Image3'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.image.name}"
