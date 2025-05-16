from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='recipes/',null=True,blank=True)
    description = models.TextField()
    course_name = models.CharField(max_length=200)
    ingredients = models.JSONField(default=list)
    instructions = models.TextField()
    is_favourite = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
