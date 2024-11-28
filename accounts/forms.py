from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import StockUser

class StockUserCreationForm(UserCreationForm):
    class Meta:
        model = StockUser
        fields = ('username','email','password1','password2')

class StockUserUpdatesForm(ModelForm):
    class Meta:
        model = StockUser
        fields = ('last_name','first_name','email')

class StockUserDetailForm(ModelForm):
    class Meta:
        model = StockUser
        fields = ('username','last_name','first_name','email')