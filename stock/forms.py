from django.forms import ModelForm
from .models import Stocker

class StockAddForm(ModelForm):
    class Meta:
        model = Stocker
        fields = ['product','stock_quantity','category']