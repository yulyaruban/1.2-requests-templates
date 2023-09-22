from django.db import models
from slugify import slugify

class Phone(models.Model):
    
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return f"name: {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)

