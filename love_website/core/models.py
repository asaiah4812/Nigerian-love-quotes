from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categries'

class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    msg = models.TextField()
    translation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} of {self.category}"

    def save(self, *args, **kwargs):
        if not self.author_id:  # Check if author is not set
            first_user = User.objects.first()
            if first_user:
                self.author = first_user
        super(Quote, self).save(*args, **kwargs)