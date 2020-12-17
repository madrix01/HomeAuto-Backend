from django.shortcuts import render
from .forms import *
from .models import *
import RPi.GPIO as GPIO
import time
from django.http import JsonResponse
import paho.mqtt.client as mqtt
import json


with open("state.json", "r") as rf:
    data = json.load(rf)
print("Hello world")

def index(request):
    client = mqtt.Client()
    client.connect('localhost', 1883, 60)
    client.loop_start()
    if request.method == "POST":
        form = IOForm(request.POST)
        if form.is_valid():
            print("Is valid")
            i = form.cleaned_data['io']
            print("i > ", i)
            if i == True:
                client.publish("/leds/esp8266", "OFF")
                data['led'] = True 
            elif i == False:
                client.publish("/leds/esp8266", "ON")
                data['led'] = False
            with open('state.json', 'w') as wf:
                json.dump(data, wf)
    else:
        form = IOForm()
    return JsonResponse({"state" : data["led"]})

def addRoomView(request):
    print(request.method)
    if request.method == "POST":
        form = addRoomForm(request.POST)
        if form.is_valid():
            roomName = form.cleaned_data['roomName']
            floor = form.cleaned_data['floor']
            x = Rooms(roomName=roomName, floor=floor)
            x.save()
    else:
        form = addRoomForm()
    content = {"total_rooms" : 0}
    return JsonResponse({"rooms" : "total_rooms"})

def roomList(request):
    ls = Rooms.objects.all()
    finalDict = []
    for x in ls:
        jsonDict = {
                "roomName" : x.roomName,
                "floor" : x.floor
                }
        finalDict.append(jsonDict)
    return JsonResponse(finalDict, safe=False)

def index1(request):
    if request.method  == "POST":
        form = IOForm(request.POST)
        if form.is_valid():
            i = form.cleaned_data['io']
            print("i > ", i)
    else:
        form = IOForm()

    return JsonResponse({"page" : "index1"})
