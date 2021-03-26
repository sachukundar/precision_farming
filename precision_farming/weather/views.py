from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
import json
from .models import Values
from precision_farming.weather_ML import predict_weather
from precision_farming.crop_ML import predict_crop
from datetime import datetime
from django.template import loader
import csv
import sys
@api_view(["POST"])
@parser_classes([JSONParser])
def api(request):
    try:
        d=request.data
        # a = Values.objects.get(id=1)
        # a.Temperature=d['Temperature']
        # a.Humidity=d['Pressure']
        # a.Pressure=d['Humidity']
        # a.Pressure=d['SMS']
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        a = Values(title="value",Temperature=d['Temperature'],Humidity=d['Pressure'],Pressure=d['Humidity'],SMS=d['SMS'],Date_Time=dt_string)
        a.save()
        print(d['Temperature'])
        print(d['Pressure'])
        print(d['Humidity'])
        print(d['SMS'])
        return Response("Parameters Sucessfully Received ")
    except ValueError as e:
        return Response(e,args[0],status.HTTP_400_BAD_REQUEST)

def weather_report(request):
    v=Values.objects.all().last()
    # print(v)
    # v=v[len(v)-1]
    # print(v.Temperature)
    # print(v.Pressure)
    # print(v.Humidity)
    # print(v.SMS)
    T,P,H,S,D=v.Temperature,v.Pressure,v.Humidity,v.SMS,v.Date_Time
    w=predict_weather(T,H,P)
    w=str(w[2:len(w)-3])
    print(w)
    # html ="<html><body>The DAte and Time is:</body></html>"+str(D)+\
    #     "<html><body><br>The temperature is:</body></html>"+str(T)+\
    #     "<html><body><br>The Pressure is:</body></html>"+str(P)+\
    #     "<html><body><br>The Humidity is:</body></html>"+str(H)+\
    #     "<html><body><br>The SMS is:</body></html>"+str(S)+\
    #     "<html><body><br>The predicted weather is:</body></html>"+str(w)
    # return HttpResponse(html)

    template = loader.get_template('weather/weather_report.html')
    contex={'T':T, 'P':P, 'H':H, 'S':S, 'D':D, 'W':str(w)}
    return HttpResponse(template.render(contex, request))


def crop_report(request):
    v=Values.objects.all().last()
    T,P,H,S,D=v.Temperature,v.Pressure,v.Humidity,v.SMS,v.Date_Time
    r,a=predict_crop(T,H,P)
    r=r[2:-2]
    a=str(float(a)*100)
    a=a[:5]
    # html ="<html><body>The DAte and Time is:</body></html>"+str(D)+\
    #     "<html><body><br>The temperature is:</body></html>"+str(T)+\
    #     "<html><body><br>The Pressure is:</body></html>"+str(P)+\
    #     "<html><body><br>The Humidity is:</body></html>"+str(H)+\
    #     "<html><body><br>The SMS is:</body></html>"+str(S)+\
    #     "<html><body><br>The predicted Crop is:</body></html>"+str(r)+\
    #     "<html><body><br>The Accuracy is:</body></html>"+str(a)
    # return HttpResponse(html)

    csv_file = csv.reader(open('precision_farming\cpdata.csv', "r"), delimiter=",")
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if r == row[4]:
            break

    template = loader.get_template('weather/predict_crop.html')
    contex={'T':T, 'P':P, 'H':H, 'S':S, 'D':D, 'R':r,'A':a,'f1':row[5],'f2':row[6],'f3':row[7],'f4':row[8],'f5':row[9]}
    return HttpResponse(template.render(contex, request))

def working(request):
    html="<html><body>working</body></html>"
    return HttpResponse(html)