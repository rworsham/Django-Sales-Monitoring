from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def boards(request):
    template = loader.get_template('board.html')
    return HttpResponse(template.render())