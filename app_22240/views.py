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
from .resources import *  # Import your resource class

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


def import_panier(request):
    if request.method == 'POST':
        pranier_resource = PanierResource()
        dataset = Dataset()
        new_panier = request.FILES.get('myfile')

        if not new_panier.name.endswith('.csv'):
            messages.info(request, 'File is not CSV type')
            return render(request, 'import.html')

        imported_data = dataset.load(new_panier.read().decode('utf-8'))
        result = pranier_resource.import_data(dataset, dry_run=True)  # Check if the data is valid

        if not result.has_errors():
            pranier_resource.import_data(dataset, dry_run=False)  # Perform the actual import
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
from django.http import HttpResponse
from import_export.formats import base_formats
from .resources import *
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
