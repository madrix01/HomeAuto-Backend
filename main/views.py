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

def ioDevice(request):
    print("Test")
    client = mqtt.Client()
    client.connect('localhost', 1883, 60)
    client.loop_start()
    if request.method == 'POST':
        form = IoDeviceForm(request.POST)
        if form.is_valid():
            boardId = form.cleaned_data['boardId']
            pinAdress = form.cleaned_data['pinAdress']
            stateTc = form.cleaned_data['stateTc']

            brd = Board.objects.get(id=boardId)
            dvc = Device.objects.get(pinAdress=pinAdress)
            if stateTc == True:
                msg = pinAdress + '/OFF'
                client.publish(brd.boardName , msg)
            elif stateTc == False:
                msg = pinAdress + '/ON'
                client.publish(brd.boardName , msg)
            dvc.state = not dvc.state
            dvc.save()
    else:
        form = IOForm()
    return JsonResponse({"page" : "working on"}, safe=False)


def addRoomView(request):
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
                "roomId" : x.id,
                "floor" : x.floor
                }
        finalDict.append(jsonDict)
    return JsonResponse(finalDict, safe=False)

def roomBoards(request, id):
    ls = Board.objects.filter(roomId=id)
    finalDict = []
    for x in ls:
        jsonDict = {
            "boardName" : x.boardName,
            "boardIp" : x.boardIp
        }
        finalDict.append(jsonDict)
    return JsonResponse(finalDict, safe=False)

def boardDevices(request, boardId):
    ls = Device.object.filter(boardId=boardId)
    finalDict = []
    for x in ls:
        jsonDict = {
            "deviceName" : x.deviceName,
            "state" : x.state,
            "pinAdress": x.pinAdress
        }
        finalDict.append(jsonDict)
    return JsonResponse(finalDict, safe=False)

def roomDevices(request, id):
    ls = Board.objects.filter(roomId=id)
    finalDict = []
    for x in ls:
        devc = Device.objects.filter(boardId = x.id)
        for y in devc:
            jsonDict = {
                "boardId" : y.boardId.id,
                "deviceName" : y.deviceName,
                "state" : y.state,
                "pinAdress" : y.pinAdress,
            }
            finalDict.append(jsonDict)
    return JsonResponse(finalDict, safe=False)

def index1(request):
    x = Device.objects.all()
    for y in x :
        print(y.deviceName, y.state)
    return JsonResponse({"page" : "index1"})
