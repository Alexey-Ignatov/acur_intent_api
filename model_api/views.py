from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from model_api.apps import intent_model


class IntentModelApi(APIView):
    @staticmethod
    def get(request):
        return Response({"intent_type": intent_model([str(request.data['context']).lower()])[0]})