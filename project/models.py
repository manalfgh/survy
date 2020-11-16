from django.db import models

# Create your models here.
class covid(models.Model):
    willaya = models.CharField(max_length=30, blank=True, null=True)
    commune = models.CharField(max_length=27, blank=True, null=True)
    willayaTravail = models.CharField(max_length=30, blank=True, null=True)
    communeTravail = models.CharField(max_length=27, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    infection = models.BooleanField()
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
	

    def __str__(self):
        return self.nom