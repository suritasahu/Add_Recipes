from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default=1)
