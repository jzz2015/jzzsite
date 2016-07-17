from django.http import HttpResponse
from django.shortcuts import render
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
