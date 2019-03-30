from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
import datetime

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return render(request, "home.html")

class CreateWorker(LoginRequiredMixin, CreateView):
    form_class = WorkerForm
    success_url = reverse_lazy('comps:list_worker')
    template_name = "create_worker.html"

class ListWorker(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "list_worker.html"

class UpdateWorker(LoginRequiredMixin, UpdateView):
    fields = ['name', 'role', 'wtype', 'salary', 'duration', 'is_active']
    model = Worker
    template_name = "update_worker.html"
    success_url = reverse_lazy('comps:list_worker')

class ToggleWorker(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        worker = Worker.objects.get(id=self.kwargs.get('pk'))
        worker.is_active = (not worker.is_active)
        worker.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_worker'))

class CreateCrop(LoginRequiredMixin, CreateView):
    form_class = CropForm
    success_url = reverse_lazy('comps:list_crop')
    template_name = "create_crop.html"

class ListCrop(LoginRequiredMixin, ListView):
    model = Crop
    context_object_name = "crop_list"
    template_name = "list_crop.html"

class UpdateCrop(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description', 'quantity', 'is_active']
    model = Crop
    template_name = "update_crop.html"
    success_url = reverse_lazy('comps:crop_worker')

class ToggleCrop(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        crop = Crop.objects.get(id=self.kwargs.get('pk'))
        crop.is_active = (not crop.is_active)
        crop.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_crop'))

class CreateEquipment(LoginRequiredMixin, CreateView):
    form_class = EquipmentForm
    success_url = reverse_lazy('comps:list_equipment')
    template_name = "create_equipment.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date = datetime.date.today()
        self.object.save()
        return super().form_valid(form)

class ListEquipment(LoginRequiredMixin, ListView):
    model = Equipment
    context_object_name = "equipment_list"
    template_name = "list_equipment.html"

class UpdateEquipment(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description', 'cost', 'is_active']
    model = Equipment
    template_name = "update_equipment.html"
    success_url = reverse_lazy('comps:list_equipment')

class ToggleEquipment(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        equipment = Equipment.objects.get(id=self.kwargs.get('pk'))
        equipment.is_active = (not equipment.is_active)
        equipment.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_equipment'))

class CreateFertilizer(LoginRequiredMixin,CreateView):
    form_class = FertilizerForm
    success_url = reverse_lazy('comps:list_fertilizer')
    template_name = "create_fertilizer.html"

class ListFertilizer(LoginRequiredMixin, ListView):
    model = Fertilizer
    context_object_name = "fertilizer_list"
    template_name = "list_fertilizer.html"

class UpdateFertilizer(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description', 'cost', 'quantity', 'crop', 'is_active']
    model = Fertilizer
    template_name = "update_fertilizer.html"
    success_url = reverse_lazy('comps:list_fertilizer')

class ToggleFertilizer(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        fertilizer = Fertilizer.objects.get(id=self.kwargs.get('pk'))
        fertilizer.is_active = (not fertilizer.is_active)
        fertilizer.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_fertilizer'))

class CreateInsecticide(LoginRequiredMixin,CreateView):
    form_class = InsecticideForm
    success_url = reverse_lazy('comps:list_insecticide')
    template_name = "create_insecticide.html"

class ListInsecticide(LoginRequiredMixin, ListView):
    model = Insecticide
    context_object_name = "insecticide_list"
    template_name = "list_insecticide.html"

class UpdateInsecticide(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description', 'cost', 'quantity', 'crop', 'is_active']
    model = Insecticide
    template_name = "update_insecticide.html"
    success_url = reverse_lazy('comps:list_insecticide')

class ToggleInsecticide(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        insecticide = Insecticide.objects.get(id=self.kwargs.get('pk'))
        insecticide.is_active = (not insecticide.is_active)
        insecticide.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_insecticide'))

class CreatePesticide(LoginRequiredMixin,CreateView):
    form_class = PesticideForm
    success_url = reverse_lazy('comps:list_pesticide')
    template_name = "create_pesticide.html"

class ListPesticide(LoginRequiredMixin, ListView):
    model = Pesticide
    context_object_name = "pesticide_list"
    template_name = "list_pesticide.html"

class UpdatePesticide(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description', 'cost', 'quantity', 'crop', 'is_active']
    model = Pesticide
    template_name = "update_pesticide.html"
    success_url = reverse_lazy('comps:list_pesticide')

class TogglePesticide(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        pesticide = Pesticide.objects.get(id=self.kwargs.get('pk'))
        pesticide.is_active = (not pesticide.is_active)
        pesticide.save()
        return HttpResponseRedirect(reverse_lazy('comps:list_pesticide'))

class CreateLoan(LoginRequiredMixin,CreateView):
    form_class = LoanForm
    success_url = reverse_lazy('comps:list_loan')
    template_name = "create_loan.html"

class ListLoan(LoginRequiredMixin, ListView):
    model = Loan
    context_object_name = "loan_list"
    template_name = "list_loan.html"

class UpdateLoan(LoginRequiredMixin, UpdateView):
    fields = ['amount', 'address', 'loan_type', 'loan_id', 'emi']
    model = Loan
    template_name = "update_loan.html"
    success_url = reverse_lazy('comps:list_loan')

class DeleteWorker(LoginRequiredMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy('comps:list_worker')

class DeleteLoan(LoginRequiredMixin, DeleteView):
    model = Loan
    success_url = reverse_lazy('comps:list_loan')

class DeletePesticide(LoginRequiredMixin, DeleteView):
    model = Pesticide
    success_url = reverse_lazy('comps:list_pesticide')

class DeleteInsecticide(LoginRequiredMixin, DeleteView):
    model = Insecticide
    success_url = reverse_lazy('comps:list_insecticide')

class DeleteFertilizer(LoginRequiredMixin, DeleteView):
    model = Fertilizer
    success_url = reverse_lazy('comps:list_fertilizer')

class DeleteCrop(LoginRequiredMixin, DeleteView):
    model = Crop
    success_url = reverse_lazy('comps:list_crop')

class DeleteProf(LoginRequiredMixin, DeleteView):
    model = History
    success_url = reverse_lazy('comps:profit_list')

class DeleteEquipment(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy('comps:list_equipment')

class CreateSale(LoginRequiredMixin,CreateView):
    form_class = SaleForm
    success_url = reverse_lazy('comps:list_sale')
    template_name = "create_sale.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date = datetime.date.today()
        self.object.save()
        return super().form_valid(form)

class ListSale(LoginRequiredMixin, ListView):
    model = Sale
    context_object_name = "sale_list"
    template_name = "list_sale.html"

class UpdateSale(LoginRequiredMixin, UpdateView):
    fields = ['crop', 'rate', 'quantity']
    model = Sale
    template_name = "update_sale.html"
    success_url = reverse_lazy('comps:list_sale')

class ProfitList(LoginRequiredMixin, ListView):
    model = History
    context_object_name = "profit_list"
    template_name = "list_profit.html"

class ProfitView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        expenditure = 0
        income = 0
        if History.objects.count() == 0:
            lastdate = datetime.datetime.strptime('Jun 1 2000  1:33PM', '%b %d %Y %I:%M%p').date()
        else:
            lastdate = History.objects.latest('id').date
        for obj in Worker.objects.all():
            if obj.is_active:
                expenditure += obj.salary * obj.duration
        for obj in Equipment.objects.all():
            if obj.date > lastdate and obj.is_active:
                expenditure += obj.cost
        for obj in Fertilizer.objects.all():
            if obj.is_active:
                expenditure += obj.cost * obj.quantity
        for obj in Insecticide.objects.all():
            if obj.is_active:
                expenditure += obj.cost * obj.quantity
        for obj in Pesticide.objects.all():
            if obj.is_active:
                expenditure += obj.cost * obj.quantity
        for obj in Loan.objects.all():
            expenditure += obj.emi
        for obj in Sale.objects.all():
            if obj.date > lastdate:
                income += obj.rate * obj.quantity
        entry = History.objects.create(month = datetime.date.today(), expenditure = expenditure, income = income,
                                profit = income - expenditure, date = datetime.date.today())
        return HttpResponseRedirect(reverse_lazy('comps:profit_list'))

        
        
        
