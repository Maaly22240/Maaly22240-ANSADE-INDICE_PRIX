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

from django.shortcuts import render
from .models import Famille, Prix
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from decimal import Decimal

def calculer_inpc_par_famille(mois, annee):
    familles = Famille.objects.all()
    resultats = []

    for famille in familles:
        # Calculate the weighted average using the ponderation field
        total_ponderation = Decimal('0')
        weighted_sum = Decimal('0')

        prix_objects = Prix.objects.filter(
            produit_id__famille_produit=famille,
            date__month=mois,
            date__year=annee
        )

        for prix_obj in prix_objects:
            # Replace 'produit_id' with the correct field name that references the Produit model
            ponderation = Decimal(str(prix_obj.produit_id.ponderation))
            valeur = Decimal(str(prix_obj.valeur))

            total_ponderation += ponderation
            weighted_sum += ponderation * valeur

        inpc = weighted_sum / total_ponderation if total_ponderation != Decimal('0') else Decimal('0')

        resultats.append({
            'date': f"{mois}/{annee}",
            'famille_produit': famille.nom,
            'inpc': inpc
        })

    return resultats

@require_GET
def afficher_inpc(request):
    if 'mois' in request.GET and 'annee' in request.GET:
        mois_str = request.GET['mois']
        annee_str = request.GET['annee']

        # Check if mois and annee are non-empty
        if mois_str and annee_str:
            try:
                mois = int(mois_str)
                annee = int(annee_str)
            except ValueError:
                return HttpResponse("Invalid month or year values")

            # Calculate INPC based on selected month and year
            resultats = calculer_inpc_par_famille(mois, annee)

            # Render the template with the results
            context = {
                'resultats': resultats
            }
            return render(request, 'inpc.html', context)

    # If the form has not been submitted or mois/annee are empty, render the empty form
    return render(request, 'inpc.html', {'resultats': []})
