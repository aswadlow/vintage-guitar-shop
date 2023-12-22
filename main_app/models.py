from django.db import models
from django.urls import reverse


# Create your models here.

class Pedal(models.Model):
  name = models.CharField(max_length=50)
  effect = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pedals_detail', kwargs={'pk': self.id})

class Guitar(models.Model):
    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    year = models.IntegerField()
    color = models.CharField(max_length = 100)
    price = models.IntegerField()

    pedals = models.ManyToManyField(Pedal)

    def __str__(self):
        return f" {self.make}, {self.model}, {self.color}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
    
class Review(models.Model):
    date = models.DateField('Review Date')
    comments = models.TextField()

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} on {self.date}"
    
    class Meta:
        ordering = ['-date']

 

    