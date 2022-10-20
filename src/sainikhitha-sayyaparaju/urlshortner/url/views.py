from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
from .forms import UrlForm
from collections import defaultdict
from .models import UrlMap
# Create your views here.

#making manually
class Encode:
    # count = 1
    maps = defaultdict(int)
    def __init__(self):
        self.count = 1
    def encode(self, id):
        const = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(const)
        res = []
        while id > 0:
            val = id % base
            res.append(const[val])
            id = id // base

        return "".join(res[::-1])

    def convert(self, url):
        if self.maps[url] != 0:
            return self.maps[url], -1
        else:
            self.maps[url] = 'http://short.ly/' + self.encode(self.count)
            self.count += 1
            return self.maps[url], 1

obj = Encode()

def home(request):
    return render(request, 'index.html')

def encode(request):
    if request.method == "POST":
        url = request.POST['url']
        type_tiny = pyshorteners.Shortener()
        short = type_tiny.tinyurl.short(url)
        mapping = UrlMap(url=url, urlShorten=short)
        mapping.save()
        context = {'url': short}
    return render(request, 'home.html', context)