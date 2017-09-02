from django.shortcuts import render,redirect, get_object_or_404
from .models import Link
from .forms import LinkDown
from pytube import YouTube


# Create your views here.


def home(request):
    return render(request, 'downloader/home.html', {})


def download(request):
    if request.method == "POST":
        form = LinkDown(request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.save()
            return redirect('result', pk=new_url.pk)
    else:
        form = LinkDown
        return render(request, 'downloader/download.html', {'form': form})


def result(request, pk):
    linkk = get_object_or_404(Link, pk=pk)
    SAVE_PATH = "E:/"  # to_do
    final = str(linkk)
    ret = " "
    link = final

    try:
        yt = YouTube(link)
    except:
        ret = "Connection Error"
    mp4files = yt.filter('mp4')
    yt.set_filename('Downloaded Video')
    d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        d_video.download(SAVE_PATH)
    except:
        ret = "Error"
    ret = 'Task Completed!'
    return render(request, 'downloader/result.html', {'ret': ret})

