from . import views
from django.urls import include, path


urlpatterns = [

    path('', views.IntentModelApi.as_view(), name='model'),

]
