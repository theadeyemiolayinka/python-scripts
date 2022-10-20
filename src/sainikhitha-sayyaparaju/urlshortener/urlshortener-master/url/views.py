from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import url_db
import shortuuid


def index(request):
    if request.method == "POST":
        og_url = request.POST.get("og_url")
        short_url = request.POST.get("short_url")
        try:
            if short_url == "":
                short_url = shortuuid.ShortUUID().random(length=5)
            url_db(og=og_url, short=short_url).save()
        except:
            msg = "This desired URL already exists or maybe your short URL is wayyyyyyy too long, please try a new one!"
            context = {"og_url": og_url, "msg": msg}
            return render(request, 'index.html', context)
        url = request.build_absolute_uri() + short_url
        context = {'url': url}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def shorten(request, short_url=""):
    u = url_db.objects.get(short=short_url)
    return redirect(u.og)
