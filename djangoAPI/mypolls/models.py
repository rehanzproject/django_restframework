from django.db import models

# Create your models here.
class Matkul(models.Model):
    id = models.IntegerField(primary_key= True)
    matkul = models.CharField(max_length= 80, blank= False)
    kodemk = models.CharField(max_length=5)

    class Meta:
        ordering = ['matkul']

    def __str__(self):
        return f"{self.matkul}:{self.kodemk}"