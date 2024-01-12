from django.db import models

class Famille(models.Model):
    nom = models.CharField(max_length=100)
class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    price_unit = models.FloatField(default=0)
    famille_produit = models.ForeignKey(Famille, on_delete=models.CASCADE)
    code = models.CharField(max_length=255,default=0)
    moyenne_ponderee = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.label  


class PointDeVent(models.Model):
    code = models.CharField(max_length=50)
    wilaya = models.CharField(max_length=50)
    moughataa = models.CharField(max_length=50)
    commune = models.CharField(max_length=50,default = 'bsk')
    gps_lat = models.IntegerField(default=0)
    gps_long = models.IntegerField(default=0)

    def __str__(self):
        return f"Point de Vent {self.code}"



class Prix(models.Model):
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    pointdevent_id = models.ForeignKey(PointDeVent, on_delete=models.CASCADE)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prix {self.id}"


class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=255,default=0)
    description = models.TextField()


class PanierProduit(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.ForeignKey(Prix, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField()

    def __str__(self):
        return f"PanierProduit {self.id}"
