from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from model_api.apps import intent_model,in_2_label
import pandas as pd


class IntentModelApi(APIView):
    @staticmethod
    def get(request):
        # intent_list = predict(str(request.data['context']).lower(),intent_model,in_2_label)
        res_l, probs = intent_model([str(request.data['context']).lower()])
        res_dict = {}
        for k, v in in_2_label.items():
            res_dict[k] = probs[0][v]

        # return Response({"intent_type":pd.Series(res_dict).sort_values().index[-1]})
        return Response({"intent_list": res_dict})