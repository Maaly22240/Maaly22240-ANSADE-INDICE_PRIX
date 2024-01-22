# urls.py

from django.urls import path
from .views import *
from . import views




urlpatterns = [
    path('', views.home),

    path('familles/', views.FamilleList.as_view(), name='famille_list'),
    path('familles/<int:pk>/', views.FamilleDetail.as_view(), name='famille_detail'),
    path('famille/create/', views.FamilleCreate.as_view(), name='famille_create'),
    path('familles/<int:pk>/delete/', views.FamilleDelete.as_view(), name='famille_delete'),
    path('familles/<int:pk>/update/', views.FamilleUpdate.as_view(), name='famille_update'),
    
    path('produits/list/', views.ProduitList.as_view(), name='produit_list'),
    path('produits/<int:pk>/', views.ProduitDetail.as_view(), name='produit_detail'),
    path('produits/create/', views.ProduitCreate.as_view(), name='produit_create'),
    path('produits/<int:pk>/update/', views.ProduitUpdate.as_view(), name='produit_update'),
    path('produits/<int:pk>/delete/', views.ProduitDelete.as_view(), name='produit_delete'),

    path('panier/', views.PanierList.as_view(), name='panier_list'),
    path('panier/<int:pk>/', views.PanierDetail.as_view(), name='panier_detail'),
    path('panier/create/', views.PanierCreate.as_view(), name='panier_create'),
    path('panier/update/<int:pk>/', views.PanierUpdate.as_view(), name='panier_update'),
    path('panier/delete/<int:pk>/', views.PanierDelete.as_view(), name='panier_delete'),

    path('point_de_vent/list/', views.PointDeVentList.as_view(), name='pointdevent_list'),
    path('point_de_vent/detail<int:pk>/', views.PointDeVentDetail.as_view(), name='pointdevent_detail'),
    path('point_de_vent/create/', views.PointDeVentCreate.as_view(), name='pointdevent_create'),
    path('point_de_vent/update/<int:pk>/', views.PointDeVentUpdate.as_view(), name='pointdevent_update'),
    path('point_de_vent/delete/<int:pk>/', views.PointDeVentDelete.as_view(), name='pointdevent_delete'),
   
    path('prix/', views.PrixList.as_view(), name='prix_list'),
    path('prix/<int:pk>/', views.PrixDetail.as_view(), name='prix_detail'),
    path('prix/create/', views.PrixCreate.as_view(), name='prix_create'),
    path('prix/update/<int:pk>/', views.PrixUpdate.as_view(), name='prix_update'),
    path('prix/delete/<int:pk>/', views.PrixDelete.as_view(), name='prix_delete'),

    path('panierproduits/', views.PanierProduitList.as_view(), name='panierproduit_list'),
    path('panierproduits/create/', views.PanierProduitCreate.as_view(), name='panierproduit_create'),
    path('panierproduits/<int:pk>/', views.PanierProduitDetail.as_view(), name='panierproduit_detail'),
    path('panierproduits/<int:pk>/edit/', views.PanierProduitUpdate.as_view(), name='panierproduit_update'),
    path('panierproduits/<int:pk>/delete/', views.PanierProduitDelete.as_view(), name='panierproduit_delete'),

    path('export/<str:model_name>/', ExportView.as_view(), name='export_view'),

    path('import_produit/', import_produit, name='import_produit'),
    path('import_panier/', import_panier, name='import_panier'),
    path('import_prix/', import_prix, name='import_prix'),
    path('import_famille/', import_famille, name='import_famille'),
    path('import_pointdevent/', import_pointdevent, name='import_pointdevent'),
    path('import_panierproduit/', import_panierproduit, name='import_panierproduit'),

    path('line_chart/<int:produit_id>/', PriceEvolutionChartView.as_view(),name='line_chart'),
    
    path('inpc/', afficher_inpc, name='inpc'),

]





