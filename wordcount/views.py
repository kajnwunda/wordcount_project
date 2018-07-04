from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            #increase
            worddic[word] += 1
        else:
            #add
            worddic[word] = 1
    sorteddic = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sorteddic})