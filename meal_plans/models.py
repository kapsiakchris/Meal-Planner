from django.db import models

class Meal(models.Model):
    """A meal the user wants to cook"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Ingredient(models.Model):
    """An ingredient to a meal"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return self.text