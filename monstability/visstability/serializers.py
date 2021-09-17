from rest_framework import serializers

from .models import Nodes, Edges

class NodesSerializer(serializers.ModelSerializer):

    label = serializers.CharField(source='label_gr')
    id = serializers.CharField(source='id_gr')
    type = serializers.CharField(source='type_gr')

    class Meta:
        model = Nodes
        fields = ('id', 'label',  'type', 'layer', 'access', 'stead', 'costdown')

class EdgesSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source='id_gr')

    class Meta:
        model = Edges
        fields = ('id', 'source',  'target', 'weight')
