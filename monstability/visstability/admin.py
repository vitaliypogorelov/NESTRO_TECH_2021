from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin import helpers
from django.conf import settings
import os


from .models import Nodes, Edges
from .grstead import GStead

FILE_MODEL = 'monstability_model.xml'

@admin.register(Nodes)
class NodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_gr', 'label_gr', 'type_gr', 'layer', 'access', 'stead', 'costdown')
    list_filter = ('type_gr', 'layer',)
    actions = ['grload_model', 'grsave_model', 'grcalc_model', 'grcalc_costdown']

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] in ('grload_model', 'grsave_model'):
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Nodes.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return admin.ModelAdmin.changelist_view(self, request, extra_context)

    def grget_model(self, AG):
        ''' загрузка графа из базы данных'''
        qrND = Nodes.objects.all()
        for ND in qrND:
            AG.add_node(
                ND.id_gr,
                type=ND.type_gr,
                label=ND.label_gr,
                layer=ND.layer,
                access=ND.access,
                stead=ND.stead,
                costdown=ND.costdown,
            )
        qrNE = Edges.objects.all()
        for NE in qrNE:
            AG.add_edge(
                NE.source,
                NE.target,
                weight=NE.weight,
                id=NE.id_gr,
            )

    def grput_model(self, AG):
        ''' выгрузка графа в базу данных'''
        if len(AG) > 0:
            Nodes.objects.all().delete()
            for node in AG.nodes.data():
                ND = Nodes.objects.create(
                    id_gr=node[0],
                    label_gr=node[1]['label'],
                    type_gr=node[1]['type'],
                    layer=node[1]['layer'],
                    access=node[1]['access'],
                    stead=node[1]['stead'],
                    costdown=node[1]['costdown'],
                )
                ND.save()

            Edges.objects.all().delete()
            for edge in AG.edges.data():
                NE = Edges.objects.create(
                    source=edge[0],
                    target=edge[1],
                    id_gr=edge[2]['id'],
                    weight=edge[2]['weight'],
                )
                NE.save()

    def grload_model(self, request, queryset):
        gr = GStead()
        gr.read_gexf(os.path.join(settings.STATIC_DIR, FILE_MODEL))
        self.grput_model(gr.G)
    grload_model.short_description = 'Загрузить модель'

    def grsave_model(self, request, queryset):
        gr = GStead()
        self.grget_model(gr.G)
        gr.write_gexf(os.path.join(settings.STATIC_DIR, FILE_MODEL))
    grsave_model.short_description = 'Сохранить модель'

    def grcalc_model(self, request, queryset):
        gr = GStead()
        self.grget_model(gr.G)
        for node in queryset:
            gr.calc_node_stead(node_id=node.id_gr)
        self.grput_model(gr.G)
    grcalc_model.short_description = 'Пересчитать показатели'

    def grcalc_costdown(self, request, queryset):
        gr = GStead()
        self.grget_model(gr.G)
        for node in queryset:
            gr.calc_costdown(node_id=node.id_gr)
        self.grput_model(gr.G)
    grcalc_costdown.short_description = 'Пересчитать стоимость простоя'


@admin.register(Edges)
class NodesAdmin(admin.ModelAdmin):
    list_display = ('id_gr', 'source', 'target', 'weight',)
    list_display_links = ('id_gr',)
#    list_filter = ('source', 'target',)
