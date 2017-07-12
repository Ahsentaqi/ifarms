from __future__ import division
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.core.context_processors import csrf
from django.views.decorators import csrf
from django.core import serializers
import os

import glob
import json
import pandas as pd


# from django.core.context_processors import csrf
import simplejson as json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import requests
import ast

import sys
import re
import os
from os.path import isfile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO

def authenticateuser(page_name):
	#path = settings.STATICFILES_DIRS+"/data/users.txt"
	#path = os.path.join(settings.STATICFILES_DIRS, 'data/users.txt')	
	#file = open(path, 'r')	
	#file = open(os.path.join(settings.MEDIA_ROOT, 'users.txt'), 'r')
	#line = file.readline()
	print "Authenticating"

def index(request):
	return render(request, 'index.html')

