from django.shortcuts import render

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")