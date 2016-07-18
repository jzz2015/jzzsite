from django.http import HttpResponse
from django.shortcuts import render
from blog.models import *
def hello(request):
	return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
	string = "jzz3"
	return render(request, 'index.html', {'username' : string})
def blog(request):
	string = "jzz2016"
	return render(request, 'blog.html', {'authorname' : string})
def writeblog(request):
	string = "jzz2016"
	return render(request, 'writeblog.html', {'authorname' : string})
def wbsub(request): 
	request.encoding='utf-8'
	if 'wb-title' in request.GET:
		wbtitle = request.GET['wb-title'].encode('utf-8')
		wbcontent = request.GET['wb-content'].encode('utf-8')
		test1 = Article(title=wbtitle,content=wbcontent)
		test1.save()
	else:
		message = 'null'
	return HttpResponse(wbtitle)