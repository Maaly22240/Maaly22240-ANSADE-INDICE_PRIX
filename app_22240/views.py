from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
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
    
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from .resources import FamilleResource, PrixResource, ProduitResource, PointDeVentResource, PanierResource, PanierProduitResource

class ExportView(View):
    def get(self, request, model_name):
        resources_map = {
            'Famille': FamilleResource,
            'Prix': PrixResource,
            'Produit': ProduitResource,
            'PointDeVent': PointDeVentResource,
            'Panier': PanierResource,
            'Panierproduit': PanierProduitResource,
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

class ImportView(View):
    template_name = 'import.html'

    def get(self, request, model_name):
        return render(request, self.template_name, {'model_name': model_name})

    def post(self, request, model_name):
        resources_map = {
            'Famille': FamilleResource,
            'Prix': PrixResource,
            'Produit': ProduitResource,
            'PointDeVent': PointDeVentResource,
            'Panier': PanierResource,
            'Panierproduit': PanierProduitResource,
        }

        resource = resources_map.get(model_name)
        if resource:
            dataset = request.FILES['file'].read().decode('utf-8')
            resource().import_data(dataset, dry_run=False)
            messages.success(request, f"Data imported successfully for model '{model_name}'.")
        else:
            messages.error(request, f"Model '{model_name}' not supported for import.")

        return render(request, self.template_name, {'model_name': model_name})


from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import Prix, Produit

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Retourne les étiquettes pour l'axe des x."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Retourne les noms des ensembles de données."""
        return ["Prix"]

    def get_data(self):
        """Retourne le jeu de données à tracer."""
        produit_id = 1  # Remplacez cela par l'ID du produit spécifique que vous souhaitez afficher

        prix_data = Prix.objects.filter(produit_id=produit_id).order_by('date')
        values = [prix.valeur for prix in prix_data]
        return [values]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
