from django.db import models


# Create your models here.
class Factory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} | '


class Production(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    sprocket_production_actual = models.IntegerField()
    sprocket_production_goal = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return f'FACTORY ID: {self.factory.id}, ACTUAL PROD: {self.sprocket_production_actual}, PROD GOAL: {self.sprocket_production_goal}, TIME: {self.time} ||| '


class Sprocket(models.Model):
    teeth = models.IntegerField()
    pitch_diameter = models.IntegerField()
    outside_diameter = models.IntegerField()
    pitch = models.IntegerField()

    def __str__(self):
        return f'SPROCKET ID: {self.id}, TEETH: {self.teeth}, PITCH DIA: {self.pitch_diameter}, OUT DIA: {self.outside_diameter}, PITCH: {self.pitch}'

