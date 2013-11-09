from django import http
from django.core import serializers
from django.views.generic.list import BaseListView
from ibge.models import UnidadeFederativa, Municipio


class StatesListView(BaseListView):
    model = UnidadeFederativa

    def render_to_response(self, context):
        data = serializers.serialize("json", self.get_queryset())
        return http.HttpResponse(data ,content_type='application/json')

class CityListView(BaseListView):
    model = Municipio

    def get_queryset(self):
        try:
            uf = self.request.GET.get('uf')
            object_list = self.model.objects.filter(uf__codigo_ibge = int(uf))
        except:
            object_list = []
            
        return object_list

    def render_to_response(self, context):
        data = serializers.serialize("json", self.get_queryset())
        return http.HttpResponse(data ,content_type='application/json')            