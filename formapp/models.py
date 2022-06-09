from django.db import models

# Create your models here.
class Registration(models.Model):
    gender_choice=(
    ('Male','Male'),
    ('Female','Female')
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=100,choices=gender_choice)
    photo=models.ImageField(upload_to='photos/')
    contact_number=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
