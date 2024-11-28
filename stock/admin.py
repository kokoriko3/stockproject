from django.contrib import admin
from .models import Stocker, Category

class StockAdmin(admin.ModelAdmin):
    # レコード一覧にIDと
    list_display = ['user','category','stock_quantity','create_date','update_date']
    readonly_fields = ('create_date','update_date')
    fieldsets = (
    ("基本情報", {
        "fields":("id", "category","stock_quantity" ),
    }),
    ("更新履歴", {
        "fields":( "create_date", "update_date", ),
    }),        
)

admin.site.register(Stocker, StockAdmin)
admin.site.register(Category)
