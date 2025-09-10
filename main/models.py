from django.db import models

class Product(models.Model):
    # 6 atribut wajib (nama field boleh disesuaikan tipis)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    # opsional
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True)
    rating = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"