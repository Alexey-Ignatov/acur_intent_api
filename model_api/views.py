from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from model_api.apps import intent_model,in_2_label
import pandas as pd

def predict(name,model,in_2_label, top=100000):
    res_l, probs = model([name.lower()])
    res_dict = {}
    for k, v in in_2_label.items():
        res_dict[k] = probs[0][v]

    return res_dict

class IntentModelApi(APIView):
    @staticmethod
    def get(request):

        res_dict = predict(str(request.data['context']).lower(),intent_model,in_2_label)
        print(res_dict)
        #return Response({"intent_type":pd.Series(res_dict).sort_values().index[-1]})
        return Response({"predict_dict": res_dict})