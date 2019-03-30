from django.forms import ModelForm, Form
from django.forms import TextInput
from .models import * 

class WorkerForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Worker

class CropForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Crop

class PesticideForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Pesticide

class InsecticideForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Insecticide

class LoanForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Loan

class EquipmentForm(ModelForm):
    class Meta:
        fields = ['name', 'description', 'cost', 'quantity', 'is_active']
        model = Equipment

class FertilizerForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Fertilizer

class SaleForm(ModelForm):
    class Meta:
        fields = ['crop', 'rate', 'quantity']
        model = Sale


