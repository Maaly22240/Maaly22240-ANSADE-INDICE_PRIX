# Dans le fichier resources.py

from import_export import resources

from .models import *

class FamilleResource(resources.ModelResource):
    class Meta:
        model = Famille

class PrixResource(resources.ModelResource):
    class Meta:
        model = Prix

class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit

class PointDeVentResource(resources.ModelResource):
    class Meta:
        model = PointDeVent

class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier

class PanierProduitResource(resources.ModelResource):
    class Meta:
        model = PanierProduit
