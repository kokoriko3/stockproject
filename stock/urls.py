from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('product_add/',views.AddView.as_view(),name='add'),
    path('catogory/<int:category>',views.CategoryView.as_view(),name='category'),
    path('stock',views.StockView.as_view(),name='stock')
]
