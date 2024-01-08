from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
@admin.register(Famille)
class FamilleAdmin(ImportExportModelAdmin):
    pass
@admin.register(Panier)
class PanierAdmin(ImportExportModelAdmin):
    pass
@admin.register(Prix)
class PrixAdmin(ImportExportModelAdmin):
    pass
@admin.register(PanierProduit)
class PanierProduitAdmin(ImportExportModelAdmin):
    pass
@admin.register(PointDeVent)
class PointDeVentAdmin(ImportExportModelAdmin):
    pass
@admin.register(Produit)
class ProduitAdmin(ImportExportModelAdmin):
    pass



