from django.contrib import admin
from .models import *
# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'name_cte',
        'name',
        'cel',
    )
    
    search_fields = ('name',)

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Color)
