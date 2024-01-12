from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from tablib import Dataset
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from import_export.formats import base_formats
from django.contrib import messages
from import_export import resources


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
            response['Content-Disposition'] = f'attachment; filename="{model_name}_export.csv"'
            return response
        else:
            messages.error(request, f"Model '{model_name}' not supported for export.")
            return render(request, 'error_template.html')



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
    


from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import Prix, Produit

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Retourne les étiquettes pour l'axe des x."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Retourne les noms des ensembles de données."""
        return ["Lait"]

    def get_data(self):
        """Retourne le jeu de données à tracer."""
        produit_id = 1  # Remplacez cela par l'ID du produit spécifique que vous souhaitez afficher

        prix_data = Prix.objects.filter(produit_id=produit_id).order_by('date')
        values = [prix.valeur for prix in prix_data]
        return [values]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()




##########################calcul d'INPC
from django.shortcuts import render
from django.views import View
from .models import PanierProduit, Produit

class CalculMoyennePonderéeView(View):
    template_name = 'calcul_moyenne_ponderee.html'

    def get(self, request, *args, **kwargs):
        # Récupérez toutes les instances PanierProduit
        panier_produits = PanierProduit.objects.all()

        # Créez un dictionnaire pour stocker les poids totaux et les sommes pondérées pour chaque produit
        totals_produits = {}

        # Parcourez les instances PanierProduit et calculez les totaux
        for panier_produit in panier_produits:
            produit_id = panier_produit.price.produit_id.id
            ponderation = panier_produit.ponderation
            prix_valeur = float(panier_produit.price.valeur)  # Convertissez en float

            # Mettez à jour le dictionnaire avec les totaux pour chaque produit
            if produit_id not in totals_produits:
                totals_produits[produit_id] = {
                    'poids_total': 0,
                    'somme_ponderee': 0,
                }

            totals_produits[produit_id]['poids_total'] += ponderation
            totals_produits[produit_id]['somme_ponderee'] += ponderation * prix_valeur  # Utilisez le float

        # Mettez à jour les instances de Produit avec la moyenne calculée
        for produit_id, totals in totals_produits.items():
            poids_total = totals['poids_total']
            somme_ponderee = totals['somme_ponderee']

            produit = Produit.objects.get(id=produit_id)
            produit.moyenne_ponderee = somme_ponderee / poids_total if poids_total != 0 else 0
            produit.save()

        # Récupérez les résultats si nécessaire
        resultats = {produit.id: produit.moyenne_ponderee for produit in Produit.objects.all()}

        # Passez les résultats au template
        context = {'resultats': resultats}
        return render(request, self.template_name, context)
