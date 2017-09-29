# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

import psutil
import json

def getSystemHealthData():
	data = {
		'cpu': psutil.cpu_percent(),
		'used_mem': psutil.virtual_memory().used,
		'total_mem': psutil.virtual_memory().total,
		'available_mem': psutil.virtual_memory().available,
		'mem_percent': psutil.virtual_memory().percent
	}
	return data

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render(getSystemHealthData(), request))

def updateData(request):
	return HttpResponse(json.dumps(getSystemHealthData()))