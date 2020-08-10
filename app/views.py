from django.shortcuts import render
from pytube import YouTube
import os
from pathlib import Path
import datetime

url = ''
def index(request):
    return render(request,'app/index.html',{})

def index2(request):
    global url
    url = request.GET.get('url')
    #try:
    now=datetime.datetime.now()
    obj = YouTube(url)
    resolutions = []
    stream_all = obj.streams.filter(progressive=True, file_extension='mp4').all()
    for i in stream_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))
    print(resolutions)
    link = url.replace("watch?v=","embed/")
    path = 'C:\\'
    return render(request,'app/down.html',{'resol':resolutions,'lnk':link,'url':url,'nw':now.strftime("%Y-%m-%d")})
    #except:
    #    return render(request,'app/sorry.html')
def download_complete(request, res):
    global url
    homedir = str(os.path.join(Path.home(), "Downloads"))
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(res).download(homedir + '/Downloads')
        return render(request, 'app/download_complete.html',{'loc':dirs,})
    else:
        return render(request, 'app/sorry.html')