from django.contrib import admin
from .models import *
admin.site.register(Famille)
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(Prix)
admin.site.register(PanierProduit)
admin.site.register(PointDeVent)
