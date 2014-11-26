import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersSerializer

from django.apps import apps
app = apps.get_app_config('app')
# Users = app.get_model('users')
# Users = get_model('app', 'users')

from django.views.generic import TemplateView
import yaml
from django.shortcuts import render_to_response

data = yaml.load(open("foo.yaml"))


class DataView(APIView):
    model = None
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):

        model = request.GET.get('model')
        self.model = app.get_model(model)
        for field in data[model]['fields']:
            self.model = app.get_model('users')

        serialize = self.serializer_class(
            self.model.objects.all(), many=True)
        return Response(serialize.data)

    # def post(self, request, *args, **kwargs):
    #     serialize = self.serializer_class(
    #         self.model)
    #     return Response(serialize.data)


class StructureDataView(APIView):
    model = None
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        model = request.GET.get('model')
        self.model = app.get_model(model)
        column_titles = []
        for field in data[model]['fields']:
            column_titles.append(field['title'])
            self.model = app.get_model('users')

        model_titles = {}
        for model in list(data.keys()):
            model_titles[model] = data[model]['title']

        return Response(json.dumps(column_titles))


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        model_titles = {}
        for model in list(data.keys()):
            model_titles[model] = data[model]['title']

        return render_to_response(self.template_name,
                                  {'models': model_titles},
                                  #  'column_titles': column_titles},
                                  )
