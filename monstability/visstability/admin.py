from django.contrib import admin

from .models import Nodes, Edges

@admin.register(Nodes)
class NodesAdmin(admin.ModelAdmin):
    list_display = ('id_gr', 'label_gr', 'type_gr', 'layer', 'access', 'stead',)
    list_display_links = ('id_gr', 'label_gr',)
    list_filter = ('type_gr', 'layer',)

@admin.register(Edges)
class NodesAdmin(admin.ModelAdmin):
    list_display = ('id_gr', 'source', 'target', 'weight',)
    list_display_links = ('id_gr',)
#    list_filter = ('source', 'target',)
