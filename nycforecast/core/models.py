from django.db import models



class City(models.Model):
    class Meta:
         verbose_name_plural = "Cities"
    name = models.CharField(max_length=200)
    popular = models.CharField(max_length=600)
    population = models.IntegerField()
    photo_path = models.URLField(max_length=200)
    def __str__(self):
        return self.name


class Prediction(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    degrees = models.IntegerField()
    tornado_percent = models.IntegerField()
    rain_percent = models.IntegerField()

    def __str__(self):
        return self.name







