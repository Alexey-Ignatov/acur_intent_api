from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from model_api.apps import intent_model,in_2_label
import pandas as pd



def predict(name,model,in_2_label):
    th1 = .9
    th2 = .15
    res_l, probs = model([name.lower()])
    res_dict = {}
    for k, v in in_2_label.items():
        res_dict[k] = probs[0][v]
    most_rel_intents_ser = pd.Series(res_dict).sort_values()[-3:]
    print(most_rel_intents_ser)
    if most_rel_intents_ser.sum() < th1:
        return ['ukn']
    if (most_rel_intents_ser > th2).any():
        return most_rel_intents_ser[most_rel_intents_ser > th2].index.tolist()
    return ['ukn']

class IntentModelApi(APIView):
    @staticmethod
    def get(request):

        intent_list = predict(str(request.data['context']).lower(),intent_model,in_2_label)
        print(intent_list)
        #return Response({"intent_type":pd.Series(res_dict).sort_values().index[-1]})
        return Response({"intent_list": intent_list})