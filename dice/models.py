from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    damage = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"

