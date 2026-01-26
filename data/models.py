from django.db import models


class ExampleModel(models.Model):
      name = models.CharField(max_length=100)
      age = models.IntegerField()
      phoneNumber = models.CharField(max_length=15)
      photo = models.ImageField(upload_to='images/')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):   
            return self.name
