from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, primary_key=True) # латинский алфавит, нижний регистр, вместо пробелов используется -/_, не допускается к названию спец. символы.
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.title
