from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import util
import encyclopedia
import markdown2
from django.http import HttpResponse
import random
import re
import os

app_name = "encyclopedia"
def index(request):
    if request.method == 'POST':
        title = request.POST.get("q")
        if util.get_entry(title):
            return redirect(entry, title)
        else:
            titles = util.list_entries()
            matches = [x for x in titles if re.search(title.lower(), x.lower())]
            return render(request, "encyclopedia/index.html", {
                "entries": matches,
                "error": True
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if util.get_entry(title):
        markdown = markdown2.Markdown()
        return render(request, "encyclopedia/entry.html", {"entry": markdown.convert(util.get_entry(title)), "title": title})
    else:
        return render(request, "encyclopedia/error.html", {"entries": util.list_entries()})

def edit(request, title):
    if request.method == 'POST':
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect(entry, title)
    else:
        if util.get_entry(title):
            return render(request, "encyclopedia/edit.html", {"entry": util.get_entry(title), "title": title})

def new(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title):
            return render(request, "encyclopedia/newError.html", {"title": title, "content": content})
        else:
            util.save_entry(title, content)
            return redirect(entry, title)
    else:
        return render(request, "encyclopedia/new.html")

def randomEntry(request):
    choice = random.choice(util.list_entries())
    return redirect(entry, choice)

def deleteEntry(request, title):
    if request.method == 'POST':
        os.remove(f"entries/{title}.md")
        return redirect(index)
    else:
        return render(request, "encyclopedia/youSure.html", {"title": title})