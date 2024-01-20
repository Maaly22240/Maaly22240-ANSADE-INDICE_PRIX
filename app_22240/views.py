from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from tablib import Dataset
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from import_export.formats import base_formats
from django.contrib import messages
from import_export import resources
from django.views import View

#########################home
def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})
def list(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})
#####################Famille

class FamilleList(ListView):
    model = Famille

class FamilleDetail(DetailView):
    model = Famille  

class FamilleCreate(CreateView):
    model = Famille
    fields = '__all__'
    success_url = reverse_lazy('famille_list')

class FamilleDelete(DeleteView):
    model = Famille
    success_url = reverse_lazy('famille_list')

class FamilleUpdate(UpdateView):
    model =  Famille
    fields = '__all__'
    success_url = reverse_lazy('famille_list')


class FamilleResource(resources.ModelResource):
    class Meta:
        model = Famille

def import_famille(request):
    if request.method == 'POST':
        famille_resource = FamilleResource()
        dataset = Dataset()
        new_famille = request.FILES.get('myfile')

        if not new_famille.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_famille.read().decode('utf-8'))
        result = famille_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            famille_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('famille_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')


################################Produit
class ProduitList(ListView):
    model = Produit

class ProduitDetail(DetailView):
    model = Produit  
    
class ProduitCreate(CreateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')

class ProduitDelete(DeleteView):
    model = Produit
    success_url = reverse_lazy('produit_list')

class ProduitUpdate(UpdateView):
    model =  Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')

class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit

def import_produit(request):
    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()
        new_produits = request.FILES.get('myfile')

        if not new_produits.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_produits.read().decode('utf-8'))
        result = produit_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            produit_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('produit_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')


################################panier
class PanierList(ListView):
    model = Panier

class PanierDetail(DetailView):
    model = Panier  

class PanierCreate(CreateView):
    model = Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')

class PanierDelete(DeleteView):
    model = Panier
    success_url = reverse_lazy('panier_list')

class PanierUpdate(UpdateView):
    model =  Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')


class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier

def import_panier(request):
    if request.method == 'POST':
        panier_resource = PanierResource()
        dataset = Dataset()
        new_panier = request.FILES.get('myfile')

        if not new_panier.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_panier.read().decode('utf-8'))
        result = panier_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            panier_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('panier_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')


################################prix
class PrixList(ListView):
    model = Prix

class PrixDetail(DetailView):
    model = Prix  

class PrixCreate(CreateView):
    model = Prix
    fields = '__all__'
    success_url = reverse_lazy('prix_list')

class PrixDelete(DeleteView):
    model = Prix
    success_url = reverse_lazy('prix_list')

class PrixUpdate(UpdateView):
    model =  Prix
    fields = '__all__'
    success_url = reverse_lazy('prix_list')


class PrixResource(resources.ModelResource):
    class Meta:
        model = Prix

def import_prix(request):
    if request.method == 'POST':
        prix_resource = PrixResource()
        dataset = Dataset()
        new_prix = request.FILES.get('myfile')

        if not new_prix.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_prix.read().decode('utf-8'))
        result = prix_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            prix_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('prix_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')

from django.http import HttpResponse
from django.views import View

class ExportView(View):
    def get(self, request, model_name):
        resources_map = {
            'famille': FamilleResource,
            'prix': PrixResource,
            'produit': ProduitResource,
            'pointdevent': PointDeVentResource,
            'panier': PanierResource,
            'panierproduit': PanierProduitResource,
        }

        resource = resources_map.get(model_name)
        if resource:
            dataset = resource().export()
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'
            return response
        else:
            messages.error(request, f"Model '{model_name}' not supported for export.")
            return render(request, 'error.html')



################################poindevent
class PointDeVentList(ListView):
    model = PointDeVent

class PointDeVentDetail(DetailView):
    model = PointDeVent  

class PointDeVentCreate(CreateView):
    model = PointDeVent
    fields = '__all__'
    success_url = reverse_lazy('pointdevent_list')

class PointDeVentDelete(DeleteView):
    model = PointDeVent
    success_url = reverse_lazy('pointdevent_list')

class PointDeVentUpdate(UpdateView):
    model =  PointDeVent
    fields = '__all__'
    success_url = reverse_lazy('pointdevent_list')


class PointDeVentResource(resources.ModelResource):
    class Meta:
        model = PointDeVent

def import_pointdevent(request):
    if request.method == 'POST':
        pointdevent_resource = PointDeVentResource()
        dataset = Dataset()
        new_pointdevent = request.FILES.get('myfile')

        if not new_pointdevent.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_pointdevent.read().decode('utf-8'))
        result = pointdevent_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            pointdevent_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('pointdevent_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')
###########################panierproduit
class PanierProduitList(ListView):
    model = PanierProduit

class PanierProduitDetail(DetailView):
    model = PanierProduit  

class PanierProduitCreate(CreateView):
    model = PanierProduit
    fields = '__all__'
    success_url = reverse_lazy('panierproduit_list')

class PanierProduitDelete(DeleteView):
    model = PanierProduit
    success_url = reverse_lazy('panierproduit_list')

class PanierProduitUpdate(UpdateView):
    model =  PanierProduit
    fields = '__all__'
    success_url = reverse_lazy('panierproduit_list')

class PanierProduitResource(resources.ModelResource):
    class Meta:
        model = PanierProduit

def import_panierproduit(request):
    if request.method == 'POST':
        panierproduit_resource = PanierProduitResource()
        dataset = Dataset()
        new_panierproduit = request.FILES.get('myfile')

        if not new_panierproduit.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_panierproduit.read().decode('utf-8'))
        result = panierproduit_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            panierproduit_resource.import_data(dataset, dry_run=False)  # Perform the actual import
            messages.success(request, 'Import successful')

            # Replace 'your_custom_view' with the actual view name or URL path
            return redirect(reverse('panierproduit_list'))
        else:
            messages.error(request, 'There was an error importing the data')

    return render(request, 'import.html')
#################################################
from django.views import View
from django.shortcuts import render, get_object_or_404
from decimal import Decimal
import json
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

class PriceEvolutionChartView(View):
    template_name = 'line_chart.html'

    def get(self, request, produit_id):
        product = get_object_or_404(Produit, id=produit_id)
        prices = Prix.objects.filter(produit_id=product).order_by('date')

        labels = []
        values = []
        mean_values = []

        current_year = None
        current_prices = []

        for price in prices:
            year = price.date.strftime('%Y')

            if current_year is None:
                current_year = year
                current_prices.append(price.valeur)
            elif current_year == year:
                current_prices.append(price.valeur)
            else:
                labels.append(current_year)
                mean_values.append(sum(current_prices) / len(current_prices))

                # Réinitialisez pour la nouvelle année
                current_year = year
                current_prices = [price.valeur]

        # Ajoutez la dernière année après la boucle
        if current_year is not None:
            labels.append(current_year)
            mean_values.append(sum(current_prices) / len(current_prices))

        labels_json = json.dumps(labels,cls=DecimalEncoder)
        values_json = json.dumps(mean_values,cls=DecimalEncoder)
        context = {
            "labels": labels_json,
            "values": values_json,
            "product": product
        }

        return render(request, self.template_name, context)
##########################calcul d'INPC

# views.py

from django.shortcuts import render
from django.views import View
from django.db.models import Avg
from decimal import Decimal
from .models import Produit, Prix, PanierProduit

class CalculMoyennePonderéeView(View):
    template_name = 'calcul_moyenne_ponderee.html'

    def get_inpc(self, month, year, produit_id):
        prix_moyen = Prix.objects.filter(date__month=month, date__year=year, produit_id=produit_id).aggregate(Avg('valeur'))['valeur__avg']
        
        if prix_moyen is not None:
            inpc = Decimal(str(prix_moyen)) * Decimal('1.1')
        else:
            inpc = None

        return inpc

    def get_queryset(self, month, year, produit_id):
        prix_filtres = Prix.objects.filter(date__month=month, date__year=year, produit_id=produit_id)

        panier_produits = PanierProduit.objects.filter(price__in=prix_filtres)

        totals_produits = {}

        for panier_produit in panier_produits:
            produit_id = panier_produit.price.produit_id.id
            ponderation = panier_produit.ponderation
            prix_valeur = float(panier_produit.price.valeur)

            if produit_id not in totals_produits:
                totals_produits[produit_id] = {
                    'poids_total': 0,
                    'somme_ponderee': 0,
                }

            totals_produits[produit_id]['poids_total'] += ponderation
            totals_produits[produit_id]['somme_ponderee'] += ponderation * prix_valeur

        for produit_id, totals in totals_produits.items():
            poids_total = totals['poids_total']
            somme_ponderee = totals['somme_ponderee']

            produit = Produit.objects.get(id=produit_id)
            produit.moyenne_ponderee = somme_ponderee / poids_total if poids_total != 0 else 0
            produit.save()

        return Produit.objects.all()

    def get(self, request, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')
        produit_id = request.GET.get('produit')

        if month and year and produit_id:
            inpc = self.get_inpc(month, year, produit_id)
            resultats = {produit.label: produit.moyenne_ponderee for produit in self.get_queryset(month, year, produit_id)}
            produit_selectionne = Produit.objects.get(id=produit_id)
        else:
            inpc = None
            resultats = None
            produit_selectionne = None

        produits = Produit.objects.all()

        context = {'resultats': resultats, 'inpc': inpc, 'produit_selectionne': produit_selectionne, 'produits': produits}
        return render(request, self.template_name, context)
