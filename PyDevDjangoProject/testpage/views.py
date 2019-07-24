from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request, n = 0, s = '', p = ''):
    return HttpResponse("""Hello, world. This is a test page.
<br>
n = {}
<br>
s = {}
<br>
path = {}
""".format(n,s,p))