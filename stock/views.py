from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Stocker, Category
from .forms import StockAddForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = 'index.html'


class StockView(ListView):
    template_name ='stock.html'
    
    def get_queryset(self):
        user = Stocker.objects.filter(user=self.request.user).order_by('-update_date')
        return user


    def post(self, request):
        if "erase" in request.POST:
            stock_pks = request.POST.getlist('delete')
            Stocker.objects.filter(pk__in=stock_pks).delete()
            url = 'stock:index'

            
        return redirect(url)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # 2つ目のモデルを指定
        ctx["category"] = Category.objects.all()
        return ctx

    
class AddView(CreateView):
    form_class = StockAddForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('stock:add')

    def form_valid(self, form):
        adddata = form.save(commit=False)
        adddata.user = self.request.user
        adddata.save()
        messages.success(self.request, '登録しました')
        return super().form_valid(form)
    

    
class CategoryView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        category_id = self.kwargs['category']
        # filter(フィールド名=id)で絞り込む
        categories = Stocker.objects.filter(category=category_id).order_by('update_date')
        return categories
    
    
    def post(self, request, category):
        if "erase" in request.POST:
            stock_pks = request.POST.getlist('delete')
            Stocker.objects.filter(pk__in=stock_pks).delete()
            url = 'stock:index'     
        return redirect(url)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # 2つ目のモデルを指定
        ctx["category"] = Category.objects.all()
        return ctx