from django.db import models

class Diplomas(models.Model):
    diplom_hash = models.CharField(max_length=256, unique=True)
    document = models.FileField()

class Alumnos(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True, unique=True)
    course = models.CharField(max_length=200)
    
    diplom = models.ForeignKey(Diplomas, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.email
