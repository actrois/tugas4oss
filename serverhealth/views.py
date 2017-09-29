# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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