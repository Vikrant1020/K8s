# from http.client import HTTPResponse
# from turtle import delay
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test, send_mail
# Create your views here.

def testing(request):
    test.delay()
    return HttpResponse('HELL')

def mail (request):
    send_mail.delay()
    return HttpResponse('SENT')
