from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, DeleteView
from .forms import StockUserCreationForm, StockUserUpdatesForm, StockUserDetailForm
from django.urls import reverse_lazy
from .models import StockUser

class SignUpView(CreateView):
    form_class = StockUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form) :
        
        user = form.save()
        self.object = user

        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"

class UserUpdateView(UpdateView):
    model = StockUser
    fields = ('last_name','first_name','email')
    template_name= 'userupdate.html'
    success_url = reverse_lazy('stock:stock' )

class UserDetailView(DetailView):
    model = StockUser
    form_class = StockUserDetailForm
    template_name = 'userdetail.html'


class PhotoDetleteView(DeleteView):
    template_name = 'userdelete.html'
    model = StockUser
    success_url = reverse_lazy('stock:index')